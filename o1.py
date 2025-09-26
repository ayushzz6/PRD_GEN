from __future__ import annotations
import os
import time
from pathlib import Path
from typing import Dict, Any

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from retrievers import get_all_retrievers
from utils import join_docs, retry, logging, save_markdown
from prompts import (
    COMPETITORS_PROMPT,
    PROBLEM_PROMPT,
    OBJECTIVES_PROMPT,
    METRICS_PROMPT,
    RISKS_PROMPT,
    US_FR_PROMPT,
    TARGET_PROMPT,
    CX_PREDICTION_PROMPT,
)

load_dotenv()

ARTIFACTS = Path.cwd() / "artifacts"
ARTIFACTS.mkdir(exist_ok=True)


class PRDGenerator:
    def __init__(self, llm_model: str = os.getenv("PRD_LLM_MODEL", "gpt-4.1"), temp: float = 0.35):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY not set in environment.")

        self.llm = ChatOpenAI(model=llm_model, temperature=temp, api_key=api_key)

        # Retrievers
        retrievers = get_all_retrievers(k=10)
        self.domain_r = retrievers.get("domain")
        self.tax_r = retrievers.get("taxonomy")
        self.comp_r = retrievers.get("compliance")
        self.ext_r = retrievers.get("external")
        self.cust_r = retrievers.get("customer_feedback")

        # Prompt pipelines
        self.problem_chain = PROBLEM_PROMPT | self.llm
        self.objectives_chain = OBJECTIVES_PROMPT | self.llm
        self.metrics_chain = METRICS_PROMPT | self.llm
        self.risks_chain = RISKS_PROMPT | self.llm
        self.fr_chain = US_FR_PROMPT | self.llm
        self.target_chain = TARGET_PROMPT | self.llm
        self.comp_chain = COMPETITORS_PROMPT | self.llm
        self.cx_chain = CX_PREDICTION_PROMPT | self.llm

    # Context retrieval
    def _get_context(self, retriever, seed: str, max_chars: int = 20000) -> str:
        if retriever is None:
            logging.warning("Retriever is None, returning empty context.")
            return "[No context]"
        try:
            docs = retriever.invoke(seed)  # updated API
            if not docs:
                logging.info(f"No docs retrieved for seed: {seed[:100]}...")
                return "[No relevant context found]"
            return join_docs(docs, max_chars=max_chars)
        except Exception:
            logging.exception("Retriever error while fetching context")
            return "[Error retrieving context]"

    @retry()
    def _run_chain(self, chain, **kwargs) -> str:
        try:
            logging.info(f"Running chain with inputs: {list(kwargs.keys())}")
            result = chain.invoke(kwargs)

            # Handle different return types
            if hasattr(result, "content"):  # ChatMessage from ChatOpenAI
                return result.content.strip()
            elif isinstance(result, dict):
                return str(result.get("output", result)).strip()
            else:
                return str(result).strip()
        except Exception:
            logging.exception("LLM chain failed")
            return "[Error generating section]"

    def generate(self, title: str, description: str) -> Dict[str, Any]:
        seed = f"{title}\n{description}"

        # Step 1: Retrieve contexts
        logging.info("Retrieving contexts...")
        domain_ctx = self._get_context(self.domain_r, seed, max_chars=18000)
        tax_ctx = self._get_context(self.tax_r, seed, max_chars=1500)
        comp_ctx = self._get_context(self.comp_r, seed, max_chars=2000)
        ext_ctx = self._get_context(self.ext_r, seed, max_chars=2000)
        cust_ctx = self._get_context(self.cust_r, seed, max_chars=5000)
        logging.info("Contexts retrieved successfully.")

        # Step 2: Generate sections
        sections = {}

        logging.info("Generating Problem Statement...")
        sections["problem"] = self._run_chain(
            self.problem_chain,
            title=title,
            description=description,
            domain_context=domain_ctx,
            external_context=ext_ctx
        )

        logging.info("Generating Objectives...")
        sections["objectives"] = self._run_chain(
            self.objectives_chain,
            title=title,
            description=description,
            domain_context=domain_ctx,
            external_context=ext_ctx
        )

        logging.info("Generating Metrics...")
        sections["metrics"] = self._run_chain(
            self.metrics_chain,
            title=title,
            description=description,
            domain_context=domain_ctx,
            taxonomy_context=tax_ctx
        )

        logging.info("Generating Target Users / Personas...")
        sections["targets"] = self._run_chain(
            self.target_chain,
            title=title,
            description=description,
            domain_context=domain_ctx,
            external_context=ext_ctx
        )

        logging.info("Generating Functional Requirements & User Stories...")
        sections["frs"] = self._run_chain(
            self.fr_chain,
            title=title,
            description=description,
            domain_context=domain_ctx,
            external_context=ext_ctx,
            feedback_context=cust_ctx
        )

        logging.info("Generating CX Predictions...")
        sections["cx"] = self._run_chain(
            self.cx_chain,
            title=title,
            description=description,
            domain_context=domain_ctx,
            feedback_context=cust_ctx,
            objectives_context=sections["objectives"],
            functional_context=sections["frs"]
        )    

        logging.info("Generating Competitors...")
        sections["competitors"] = self._run_chain(
            self.comp_chain,
            title=title,
            description=description,
            domain_context=domain_ctx,
            external_context=ext_ctx
        )

        logging.info("Generating Risks & Dependencies...")
        sections["risks"] = self._run_chain(
            self.risks_chain,
            title=title,
            description=description,
            compliance_context=comp_ctx,
            domain_context=domain_ctx,
            external_context=ext_ctx
        )

        # Step 3: Assemble Markdown
        md_lines = [
            f"# {title}",
            "## Problem Statement", sections["problem"],
            "## Goals & Objectives", sections["objectives"],
            "## Lead & Lag Metrics", sections["metrics"],
            "## Target Users / Personas", sections["targets"],
            "## Functional Requirements and User Stories", sections["frs"],
            "## CX Predictions", sections["cx"],
            "## Competitors", sections["competitors"],
            "## Risks & Dependencies", sections["risks"],
        ]

        assembled_md = "\n\n".join(md_lines)
        filename = f"{title.replace(' ', '_')}_{int(time.time())}.md"
        path = ARTIFACTS / filename
        save_markdown(path, assembled_md)

        return {**sections, "markdown": assembled_md, "path": str(path)}
