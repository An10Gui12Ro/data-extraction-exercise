"""Document classifier — determines if a document is a will or a trust."""

from src.client import call_llm
from src.prompts import CLASSIFICATION_PROMPT
from src.schemas import ClassificationResult


def classify_document(document_text: str) -> str:
    """
    Classify a document as either 'will' or 'trust'.

    Args:
        document_text: The full text of the document.

    Returns:
        Either "will" or "trust" (lowercase).

    TODO:
        1. Call the LLM using call_llm() with the CLASSIFICATION_PROMPT
           and ClassificationResult as the response_format
        2. Extract the classification string from the parsed result
        3. Return it
    """
    # TODO: Implement this function (~2-3 lines)
    response = call_llm(CLASSIFICATION_PROMPT, document_text, ClassificationResult)
    return response.document_type
