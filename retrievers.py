# phase3_rag/retriever.py
import os
from pathlib import Path
from typing import Dict

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from utils import logging
from  dotenv import load_dotenv

load_dotenv()

# Config
BASE = Path.cwd()
VECTOR_ROOT = BASE / "vectorstore"
EMBED_MODEL = os.getenv("PRD_EMBED_MODEL", "text-embedding-3-small")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_KEY:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your environment variables or .env file.")


def load_retriever(collection: str, persist_dir: Path, k: int = 21):
    """Load a retriever for a given Chroma collection."""
    try:
        embeddings = OpenAIEmbeddings(model=EMBED_MODEL, openai_api_key=OPENAI_KEY)
        vs = Chroma(
            persist_directory=str(persist_dir),
            embedding_function=embeddings,
            collection_name=collection
        )
        logging.info(f"Loaded retriever for collection: {collection}")
        return vs.as_retriever(search_kwargs={"k": k})
    except Exception as e:
        logging.exception(f"Failed to load retriever for {collection}")
        raise



def get_all_retrievers(k: int = 21) -> Dict[str, object]:
    retrievers = {}
    try:
        retrievers["compliance"] = load_retriever("compliance", VECTOR_ROOT / "compliance", k)
    except Exception as e:
        logging.warning(f"Compliance retriever not available: {e}")

    try:
        retrievers["taxonomy"] = load_retriever("taxonomy", VECTOR_ROOT / "taxonomy", k)
    except Exception as e:
        logging.warning(f"Taxonomy retriever not available: {e}")

    try:
        retrievers["domain"] = load_retriever("domain", VECTOR_ROOT / "domain", k)
    except Exception as e:
        logging.warning(f"Domain retriever not available: {e}")

    try:
        retrievers["external"] = load_retriever("external", VECTOR_ROOT / "external", k)
    except Exception as e:
        logging.warning(f"External retriever not available: {e}")

    try:
        retrievers["customer_feedback"] = load_retriever("customer_feedback", VECTOR_ROOT / "customer_feedback", k)
    except Exception as e:
        logging.warning(f"Customer Feedback retriever not available: {e}")

    if not retrievers:
        raise RuntimeError("No retrievers could be loaded. Please run indexer.py and deep_research.py first.")

    return retrievers

