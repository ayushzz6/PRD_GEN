# phase3_rag/utils.py
import time
import logging
import asyncio
from typing import Callable, Any, List
from functools import wraps
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def retry(retries: int = 3, backoff: float = 1.0):
    """Retry decorator for sync and async functions with exponential backoff."""

    def decorator(fn: Callable[..., Any]):
        @wraps(fn)
        def sync_wrapper(*args, **kwargs):
            last_exc = None
            delay = backoff
            for i in range(retries):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    logging.warning(f"[Retry {i+1}/{retries}] {fn.__name__} failed: {e}")
                    time.sleep(delay)
                    delay *= 2
            logging.error(f"All retries failed for {fn.__name__}: {last_exc}")
            raise last_exc

        @wraps(fn)
        async def async_wrapper(*args, **kwargs):
            last_exc = None
            delay = backoff
            for i in range(retries):
                try:
                    return await fn(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    logging.warning(f"[Retry {i+1}/{retries}] {fn.__name__} failed: {e}")
                    await asyncio.sleep(delay)
                    delay *= 2
            logging.error(f"All retries failed for {fn.__name__}: {last_exc}")
            raise last_exc

        return async_wrapper if asyncio.iscoroutinefunction(fn) else sync_wrapper

    return decorator


def join_docs(docs, max_chars: int = 2000) -> str:
    """Concatenate retrieved doc contents, honoring max_chars."""
    parts = []
    total = 0
    for d in docs:
        txt = getattr(d, "page_content", str(d)).strip()
        if not txt:
            continue
        if total + len(txt) > max_chars:
            parts.append(txt[: max_chars - total])  # truncate last chunk
            break
        parts.append(txt)
        total += len(txt)
    return "\n\n---\n\n".join(parts)


def save_markdown(path: Path, md_text: str):
    """Save markdown text to a file with UTF-8 encoding."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(md_text, encoding="utf-8")
    logging.info(f"Saved PRD markdown at {path}")


def preview_docs(docs: List[Any], top_n: int = 3):
    """
    Print a preview of the top retrieved docs for debugging.

    Args:
        docs (List[Any]): List of retrieved documents.
        top_n (int): Number of docs to preview (default=3).
    """
    if not docs:
        logging.info("No documents retrieved to preview.")
        return

    logging.info(f"Previewing top {min(top_n, len(docs))} retrievals:")
    for i, d in enumerate(docs[:top_n], 1):
        txt = getattr(d, "page_content", str(d)).strip()
        logging.info(
            f"\n--- Doc {i} ---\n{txt[:500]}{'...' if len(txt) > 500 else ''}\n"
        )
