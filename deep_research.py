
import os
import json
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from utils import logging
from indexer import _split_texts_to_docs
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

BASE = Path.cwd()
DATA_DIR = BASE / "data"
VECTOR_ROOT = BASE / "vectorstore" / "external"
DATA_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_ROOT.mkdir(parents=True, exist_ok=True)


def run_deep_research(title: str, description: str, model: str = "o3-mini") -> Path:
    """
    Runs deep research with O3/O4, saves structured JSON, and indexes into vector DB.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    query = f"""
You are an expert fintech research assistant for Angel One. Use the product Title and Description
below to perform **product-specific deep research**. Your job is to return a single, strict JSON
document (no markdown, no extra commentary) that follows the schema exactly. If you cannot find
evidence for a claim, leave the field as an empty string or empty list.

Product:
- Title: {title}
- Description: {description}

Scope (use Title & Description to focus research):
1) Market landscape & size: market segments, adoption trends, target geographies, likely TAM / SAM estimates (if available) , it should be product-specific , take the title and description into account for reference.
2) Competitors & benchmarks: direct Indian competitors (e.g. Zerodha, Upstox, others) and relevant global leaders — compare features and KPIs relevant to this product-specific , take the title and description into account for reference.
3) Benchmarks: include industry latency, execution, and compliance-cost references where applicable (cite sources),  it should be product-specific , take the title and description into account for reference.
4) Data requirements: explicitly list what datasets the product needs (tick-level, order book, trades, execution logs, user behavioral events, etc.).
5) Opportunities: product-specific growth areas, differentiation ideas, infra improvements, customer experience enhancements — tie them to the product Title/Description,  it should be product-specific , take the title and description into account for reference.
6) Risks: technical (latency, model drift, data quality), business (adoption, churn), regulatory (SEBI/DPDP/other compliance flags),  it should be product-specific , take the title and description into account for reference.
7) Recommendations: prioritized short-term vs long-term next steps for the product team,  it should be product-specific , take the title and description into account for reference.
8) Competitors: list key competitors with brief descriptions, the derived market share, strengths and weaknesses, all this should be product-specific , take the title and description into account for reference.
Return a single JSON object strictly using this schema (no surrounding text):

{{
  "title": "{title}",
  "description": "{description}",
  "timestamp": "<ISO-8601 UTC timestamp>",
  "sources": [
    {{
      "url": "<reference link if available>",
      "snippet": "<short excerpt or insight from that source>",
      "accessed": "<YYYY-MM-DD>"
    }}
  ],
  "sections": {{
    "executive_summary": "Concise one-paragraph overview of findings (<=120 words)",
    "market_context": "Market size, adoption trends, competitors, adoption barriers (product-specific)",
    "regulatory_flags": "Relevant SEBI/RBI/DPDP/GDPR or other compliance points (product-specific)",
    "data_requirements": ["list of required datasets (tick-level, order book, transactions, user events, etc.)"],
    "risks": ["technical risks", "business risks", "regulatory risks"],
    "opportunities": ["growth areas, differentiation, infra improvements, CX improvements"],
    "benchmarks": "Latency benchmarks, execution benchmarks, compliance cost references (cite where possible)",
    "recommendations": ["prioritized actions (short/medium/long)"]
    "competitors": [" list key competitors with brief descriptions, the derived market share, strengths and weaknesses, all this should be product-specific , take the title and description into account for reference."]
  }},
  "entities": [
    {{
      "type": "regulation|competitor|partner|technology",
      "id": "<unique id or reference>",
      "text": "<brief description>"
    }}
  ]
}}

Guidelines:
- Every factual claim should have at least one supporting 'source' entry in the 'sources' array.
- Use the product Title and Description to focus research, do not do generic research, make it product-specific , take the title and description into account for reference.
- Keep executive_summary <= 120 words.
- If uncertain or unavailable, use empty string "" or [].
- Strictly valid JSON only. Do NOT wrap in markdown or add commentary.
"""

    logging.info("Running deep research with O3/O4...")
    response = client.responses.create(
        model=model,
        input=query,
        reasoning={"effort": "medium"},
        max_output_tokens=10000,
    )

    research_text = response.output_text.strip()

    # Save structured JSON
    json_path = DATA_DIR / "research.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json.loads(research_text), f, indent=2)

    # Index to vector DB
    docs = _split_texts_to_docs([(research_text, {"source": "o3_research"})])
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    Chroma.from_documents(
        docs, embeddings,
        persist_directory=str(VECTOR_ROOT),
        collection_name="external"
    )
    
    logging.info("Deep research indexed into vectorstore/external.")
    return json_path




'''


# phase3_rag/deep_research.py
from __future__ import annotations
import os
import time
import json
import re
from pathlib import Path
from typing import Optional, Dict, Any

import openai
from dotenv import load_dotenv

# Optional: Chroma indexing (requires langchain_openai + chroma)
try:
    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores import Chroma
    CHROMA_AVAILABLE = True
except Exception:
    CHROMA_AVAILABLE = False

load_dotenv()

ARTIFACTS = Path.cwd() / "artifacts"
ARTIFACTS.mkdir(parents=True, exist_ok=True)

# Defaults
DEFAULT_CHAT_MODEL = "o3-mini"           # or "o3-pro", "gpt-4o", "gpt-4.1"
DEFAULT_EMBED_MODEL = os.getenv("PRD_EMBED_MODEL", "text-embedding-3-small")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set in environment variables or .env")

openai.api_key = OPENAI_API_KEY


def _extract_json_from_text(text: str) -> Optional[str]:
    """
    Try to extract the first JSON object from a text blob.
    Returns the JSON string or None.
    """
    # First try to find {...} region that looks like top-level JSON
    # This regex matches the outermost JSON object (greedy braces).
    pattern = re.compile(r"\{(?:[^{}]|(?R))*\}", re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(0)
    # fallback: find first bracketed array/object
    bracket_match = re.search(r"(\[.*\])", text, re.DOTALL)
    if bracket_match:
        return bracket_match.group(1)
    return None


def run_deep_research(
    title: str,
    description: str,
    model: str = DEFAULT_CHAT_MODEL,
    save_and_index: bool = True,
    chroma_persist_dir: Optional[Path] = None,
    max_retries: int = 2,
) -> Path:
    """
    Run a deep research study using an OpenAI chat model and return path to saved JSON file.
    - title, description: product context (100-200 words recommended in description)
    - model: chat model name (e.g. 'o3-mini', 'o3-pro', 'gpt-4o', 'gpt-4.1')
    - save_and_index: if True and chroma is available, index the returned JSON summary into Chroma
    - chroma_persist_dir: optional Path to store vectorstore (defaults to ./vectorstore/research)
    Returns: Path to the saved JSON file.
    """

    if not title or not description:
        raise ValueError("Both title and description must be provided.")

    prompt = f"""
You are an expert fintech research assistant for Angel One. Use the product Title and Description
below to perform **product-specific deep research**. Your job is to return a single, strict JSON
document (no markdown, no extra commentary) that follows the schema exactly. If you cannot find
evidence for a claim, leave the field as an empty string or empty list.

Product:
- Title: {title}
- Description: {description}

Scope (use Title & Description to focus research):
1) Market landscape & size: market segments, adoption trends, target geographies, likely TAM / SAM estimates (if available) , it should be product-specific , take the title and description into account for reference.
2) Competitors & benchmarks: direct Indian competitors (e.g. Zerodha, Upstox, others) and relevant global leaders — compare features and KPIs relevant to this product-specific , take the title and description into account for reference.
3) Benchmarks: include industry latency, execution, and compliance-cost references where applicable (cite sources),  it should be product-specific , take the title and description into account for reference.
4) Data requirements: explicitly list what datasets the product needs (tick-level, order book, trades, execution logs, user behavioral events, etc.).
5) Opportunities: product-specific growth areas, differentiation ideas, infra improvements, customer experience enhancements — tie them to the product Title/Description,  it should be product-specific , take the title and description into account for reference.
6) Risks: technical (latency, model drift, data quality), business (adoption, churn), regulatory (SEBI/DPDP/other compliance flags),  it should be product-specific , take the title and description into account for reference.
7) Recommendations: prioritized short-term vs long-term next steps for the product team,  it should be product-specific , take the title and description into account for reference.

Return a single JSON object strictly using this schema (no surrounding text):

{{
  "title": "{title}",
  "description": "{description}",
  "timestamp": "<ISO-8601 UTC timestamp>",
  "sources": [
    {{
      "url": "<reference link if available>",
      "snippet": "<short excerpt or insight from that source>",
      "accessed": "<YYYY-MM-DD>"
    }}
  ],
  "sections": {{
    "executive_summary": "Concise one-paragraph overview of findings (<=120 words)",
    "market_context": "Market size, adoption trends, competitors, adoption barriers (product-specific)",
    "regulatory_flags": "Relevant SEBI/RBI/DPDP/GDPR or other compliance points (product-specific)",
    "data_requirements": ["list of required datasets (tick-level, order book, transactions, user events, etc.)"],
    "risks": ["technical risks", "business risks", "regulatory risks"],
    "opportunities": ["growth areas, differentiation, infra improvements, CX improvements"],
    "benchmarks": "Latency benchmarks, execution benchmarks, compliance cost references (cite where possible)",
    "recommendations": ["prioritized actions (short/medium/long)"]
  }},
  "entities": [
    {{
      "type": "regulation|competitor|partner|technology",
      "id": "<unique id or reference>",
      "text": "<brief description>"
    }}
  ]
}}

Guidelines:
- Every factual claim should have at least one supporting 'source' entry in the 'sources' array.
- Use the product Title and Description to focus research, do not do generic research, make it product-specific , take the title and description into account for reference.
- Keep executive_summary <= 120 words.
- If uncertain or unavailable, use empty string "" or [].
- Strictly valid JSON only. Do NOT wrap in markdown or add commentary.
"""

    # Chat completion call with retries
    attempt = 0
    raw_response_text = None
    while attempt <= max_retries:
        attempt += 1
        try:
            resp = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a rigorous research assistant; answer in strict JSON only."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.0,
                max_tokens=4500,
            )
            # Extract model text
            raw_response_text = resp["choices"][0]["message"]["content"]
            # Try parsing directly
            try:
                parsed = json.loads(raw_response_text)
                research_obj = parsed
                break
            except Exception:
                # Try to extract JSON substring (if model added explanation text)
                json_text = _extract_json_from_text(raw_response_text)
                if json_text:
                    try:
                        research_obj = json.loads(json_text)
                        break
                    except Exception:
                        # No valid JSON yet; will retry
                        pass

            # If here, not valid JSON — retry (with lower temperature still 0)
            if attempt <= max_retries:
                # add an assistant message nudging strict JSON format
                prompt_followup = (
                    "The previous response did not contain strict JSON. Reply with the exact JSON object only, "
                    "no explanation. Use the schema exactly as provided."
                )
                # continue loop to retry – add follow-up system message in next request
                continue
            else:
                raise ValueError("Failed to produce valid JSON from model response.")

        except openai.error.OpenAIError as e:
            if attempt > max_retries:
                raise
            else:
                time.sleep(1.0 * attempt)
                continue

    # At this point research_obj should exist
    if raw_response_text is None:
        raise RuntimeError("No response received from model.")

    # If research_obj not set (safety)
    if "research_obj" not in locals():
        # final attempt to extract
        json_text = _extract_json_from_text(raw_response_text or "")
        if not json_text:
            raise RuntimeError("Couldn't parse JSON from model output.")
        research_obj = json.loads(json_text)

    # Add timestamp if missing
    if not research_obj.get("timestamp"):
        research_obj["timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # Save JSON to artifacts
    ts = int(time.time())
    safe_title = re.sub(r"[^\w\-]+", "_", title)[:80]
    filename = ARTIFACTS / f"{safe_title}_deep_research_{ts}.json"
    filename.write_text(json.dumps(research_obj, indent=2, ensure_ascii=False), encoding="utf-8")

    # Optional: Index short summary into Chroma for retrieval (if requested and available)
    if save_and_index and CHROMA_AVAILABLE:
        try:
            # make a small textual summary for embedding: executive_summary + market_context + first source snippet
            exec_sum = research_obj.get("sections", {}).get("executive_summary", "") or ""
            market = research_obj.get("sections", {}).get("market_context", "") or ""
            first_source_snippet = ""
            if research_obj.get("sources"):
                first_source_snippet = research_obj["sources"][0].get("snippet", "")

            index_text = (
                f"Title: {title}\nExecutive summary: {exec_sum}\nMarket context: {market}\nSample source: {first_source_snippet}"
            )
            embeddings = OpenAIEmbeddings(model=DEFAULT_EMBED_MODEL)
            persist_dir = chroma_persist_dir or (Path.cwd() / "vectorstore" / "research")
            persist_dir.mkdir(parents=True, exist_ok=True)
            docs = [
                # Using a simple doc with metadata to store the JSON path and some metadata
                {
                    "page_content": index_text,
                    "metadata": {"title": title, "path": str(filename), "timestamp": research_obj.get("timestamp", "")},
                }
            ]
            # Chroma expects Document objects in some wrappers; langchain_community Chroma.from_documents accepts list of dicts or Document.
            Chroma.from_documents(docs, embeddings, persist_directory=str(persist_dir), collection_name="deep_research")
        except Exception:
            # Indexing is optional — do not fail the function on index errors
            import traceback
            logging = None
            try:
                from utils import logging as ulogging

                ulogging.exception("Failed to index research summary into Chroma.")
            except Exception:
                print("Failed to index research summary into Chroma (no logger available).")
                print(traceback.format_exc())

    return filename
'''
