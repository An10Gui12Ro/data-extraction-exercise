"""
Data models for document classification and extraction. Uses Pydantic for OpenAI structured outputs.
"""

from pydantic import BaseModel
from typing import Literal


class ClassificationResult(BaseModel):
    """
    Schema for document classification response.

    TODO: Define the field(s) needed to classify a document as "will" or "trust".
    Hint: You need a single field that constrains the LLM to respond with
    exactly "will" or "trust". Look into typing.Literal.
    """
    # TODO: Define the field(s) for this schema (~1-2 lines)
    document_type: Literal["will", "trust"]


# --- DO NOT MODIFY BELOW THIS LINE ---


class WillExtraction(BaseModel):
    """Extraction schema for will documents."""
    document_type: str  # always "will"
    testator: str  # full name of the person whose will it is
    executors: list[str]  # list of executor full names
    assets: list[str]  # list of asset descriptions
    date: str  # execution date in YYYY-MM-DD format
    state: str  # governing state (full name, e.g. "California")


class TrustExtraction(BaseModel):
    """Extraction schema for trust documents."""
    document_type: str  # always "trust"
    grantors: list[str]  # list of grantor/settlor full names
    trustees: list[str]  # list of CURRENT trustee full names (not successors)
    assets: list[str]  # list of asset descriptions
    date: str  # execution date in YYYY-MM-DD format
    state: str  # governing state (full name, e.g. "California")
