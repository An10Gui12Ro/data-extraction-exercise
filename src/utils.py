"""Utility functions for normalizing extracted data."""

import re


def normalize_name(name: str) -> str:
    """
    Normalize a person's name for comparison.

    Rules:
        - Strip leading/trailing whitespace
        - Remove titles/prefixes: Mr., Mrs., Ms., Dr., Jr., Sr., III, II, Esq.
        - Remove extra spaces between words
        - Convert to title case

    Examples:
        "  Dr. John  Michael Smith Jr. " -> "John Michael Smith"
        "JANE DOE" -> "Jane Doe"
        "mr. bob jones" -> "Bob Jones"

    TODO: Implement this function.
    """
    # TODO: Implement (~5-8 lines)
    pass


def normalize_date(date_str: str) -> str:
    """
    Normalize a date string to YYYY-MM-DD format.

    Should handle common formats:
        "January 15, 2023" -> "2023-01-15"
        "01/15/2023" -> "2023-01-15"
        "2023-01-15" -> "2023-01-15"

    TODO: Implement this function.
    """
    # TODO: Implement (~5-8 lines)
    pass
