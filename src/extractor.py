"""Data extraction from classified documents."""

from src.client import call_llm
from src.classifier import classify_document
from src.prompts import WILL_EXTRACTION_PROMPT, TRUST_EXTRACTION_PROMPT
from src.schemas import WillExtraction, TrustExtraction


def extract_will(document_text: str) -> WillExtraction:
    """
    Extract structured data from a will document.

    TODO:
        1. Call the LLM using call_llm() with WILL_EXTRACTION_PROMPT
           and WillExtraction as the response_format
        2. Return the parsed result
    """
    # TODO: Implement this function (~2-3 lines)
    pass


def extract_trust(document_text: str) -> TrustExtraction:
    """
    Extract structured data from a trust document.

    TODO:
        1. Call the LLM using call_llm() with TRUST_EXTRACTION_PROMPT
           and TrustExtraction as the response_format
        2. Return the parsed result
    """
    # TODO: Implement this function (~2-3 lines)
    pass


def process_document(document_text: str) -> WillExtraction | TrustExtraction:
    """
    Full pipeline: classify a document and extract its data.

    TODO:
        1. Use classify_document() to determine the document type
        2. Based on the type, call extract_will() or extract_trust()
        3. Return the extraction result
    """
    # TODO: Implement this function (~5 lines)
    pass
