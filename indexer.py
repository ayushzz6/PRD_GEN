from __future__ import annotations
import os
import json
import logging
from pathlib import Path
from typing import List, Tuple, Dict

import pandas as pd
from dotenv import load_dotenv
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

from utils import retry  # Updated path for your utils.py

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Config
BASE = Path.cwd()
DATA_DIR = BASE / "data"
VECTOR_ROOT = BASE / "vectorstore"
EMBED_MODEL = os.getenv("PRD_EMBED_MODEL", "text-embedding-3-small")


def _split_texts_to_docs(
    texts_with_meta: List[Tuple[str, dict]],
    chunk_size: int = 1200,
    overlap: int = 200
) -> List[Document]:
    """Split texts into chunks and convert to LangChain Documents with metadata."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    docs: List[Document] = []
    for text, meta in texts_with_meta:
        for chunk in splitter.split_text(text):
            docs.append(Document(page_content=chunk, metadata=meta))
    return docs


@retry()
def index_compliance(json_path: Path = DATA_DIR / "complaince.json", persist_dir: Path = VECTOR_ROOT / "compliance") -> None:
    if not json_path.exists():
        logging.warning(f"Compliance JSON not found at {json_path}. Skipping.")
        return

    raw = json.loads(json_path.read_text(encoding="utf-8"))
    texts_with_meta: List[Tuple[str, dict]] = []

    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                text = " | ".join([f"{k}: {v}" for k, v in item.items()])
                texts_with_meta.append((text, item))
            else:
                texts_with_meta.append((str(item), {"raw": str(item)}))
    elif isinstance(raw, dict):
        text = " | ".join([f"{k}: {v}" for k, v in raw.items()])
        texts_with_meta.append((text, raw))

    docs = _split_texts_to_docs(texts_with_meta)
    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)
    persist_dir.mkdir(parents=True, exist_ok=True)
    Chroma.from_documents(docs, embeddings, persist_directory=str(persist_dir), collection_name="compliance")
    logging.info(f"Indexed {len(docs)} compliance chunks.")


@retry()
def index_taxonomy(csv_path: Path = DATA_DIR / "PRD - REPO_Explanation - Sheet1 (1).csv", persist_dir: Path = VECTOR_ROOT / "taxonomy") -> None:
    if not csv_path.exists():
        logging.warning(f"Taxonomy CSV not found at {csv_path}. Skipping.")
        return

    df = pd.read_csv(csv_path).fillna("")
    texts_with_meta: List[Tuple[str, dict]] = []

    for _, row in df.iterrows():
        row_dict = row.to_dict()
        text = " | ".join([f"{k}: {v}" for k, v in row_dict.items()])
        texts_with_meta.append((text, row_dict))

    docs = _split_texts_to_docs(texts_with_meta)
    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)
    persist_dir.mkdir(parents=True, exist_ok=True)
    Chroma.from_documents(docs, embeddings, persist_directory=str(persist_dir), collection_name="taxonomy")
    logging.info(f"Indexed {len(docs)} taxonomy rows.")


@retry()
def index_domain(domain_json: Path = DATA_DIR / "angelone_scraped_kb.json", persist_dir: Path = VECTOR_ROOT / "domain") -> None:
    if not domain_json.exists():
        logging.warning(f"Domain KB not found at {domain_json}. Skipping.")
        return

    raw = json.loads(domain_json.read_text(encoding="utf-8"))
    texts_with_meta: List[Tuple[str, dict]] = []

    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                text = " | ".join([f"{k}: {v}" for k, v in item.items()])
                texts_with_meta.append((text, item))
            else:
                texts_with_meta.append((str(item), {"raw": str(item)}))
    elif isinstance(raw, dict):
        text = " | ".join([f"{k}: {v}" for k, v in raw.items()])
        texts_with_meta.append((text, raw))

    docs = _split_texts_to_docs(texts_with_meta)
    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)
    persist_dir.mkdir(parents=True, exist_ok=True)
    Chroma.from_documents(docs, embeddings, persist_directory=str(persist_dir), collection_name="domain")
    logging.info(f"Indexed {len(docs)} domain chunks.")


@retry()
def index_external(json_path: Path = DATA_DIR / "research.json", persist_dir: Path = VECTOR_ROOT / "external") -> None:
    if not json_path.exists():
        logging.warning(f"External research JSON not found at {json_path}. Skipping.")
        return

    raw = json.loads(json_path.read_text(encoding="utf-8"))
    text = raw.get("content", "")
    metadata = {"title": raw.get("title"), "description": raw.get("description")}
    texts_with_meta = [(text, metadata)]

    docs = _split_texts_to_docs(texts_with_meta)
    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)
    persist_dir.mkdir(parents=True, exist_ok=True)
    Chroma.from_documents(docs, embeddings, persist_directory=str(persist_dir), collection_name="external")
    logging.info(f"Indexed {len(docs)} external research chunks.")


@retry()
def index_customer_feedback(csv_path: Path = DATA_DIR / "feedback.xlsx", persist_dir: Path = VECTOR_ROOT / "customer_feedback") -> None:
    if not csv_path.exists():
        logging.warning(f"Customer feedback file not found at {csv_path}. Skipping.")
        return

    # Pandas can handle both CSV and Excel
    if csv_path.suffix in [".xlsx", ".xls"]:
        df = pd.read_excel(csv_path).fillna("")
    else:
        df = pd.read_csv(csv_path).fillna("")

    texts_with_meta: List[Tuple[str, dict]] = []
    for _, row in df.iterrows():
        row_dict = row.to_dict()
        comment_text = str(row_dict.get("comments", "")).strip()
        if not comment_text:
            continue
        texts_with_meta.append((comment_text, row_dict))

    docs = _split_texts_to_docs(texts_with_meta)
    embeddings = OpenAIEmbeddings(model=EMBED_MODEL)
    persist_dir.mkdir(parents=True, exist_ok=True)
    Chroma.from_documents(docs, embeddings, persist_directory=str(persist_dir), collection_name="customer_feedback")
    logging.info(f"Indexed {len(docs)} customer feedback comments.")


def index_all() -> None:
    errors: Dict[str, str] = {}

    for fn_name, fn in [
        ("compliance", index_compliance),
        ("taxonomy", index_taxonomy),
        ("domain", index_domain),
        ("external", index_external),
        ("customer_feedback", index_customer_feedback),
    ]:
        try:
            fn()
        except Exception as e:
            errors[fn_name] = str(e)

    if errors:
        logging.warning(f"Indexing finished with errors: {errors}")
    else:
        logging.info("Indexing finished successfully for all KBs.")


if __name__ == "__main__":
    print("Starting KB indexing...")
    try:
        index_all()
        print("Indexing completed. Vectorstores are ready in ./vectorstore/")
    except Exception as e:
        print(f"Indexing failed: {e}")
