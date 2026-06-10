"""Utility functions for normalizing extracted data."""

import re
from datetime import datetime


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
    if not name or not isinstance(name, str):
        return ""
    pattern = r'(Mr\.|Mrs\.|Ms\.|Dr\.|Jr\.|Sr\.|III|II|Esq\.)'
    name = name.strip()
    name = re.sub(pattern, "", name, flags=re.IGNORECASE)
    name = " ".join(name.split())
    return name.title()


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
    # Actualmente se cubren los casos puestos en el docstring mas 2 extras: "%d-%m-%Y" y "%b %d, %Y"
    # Sería buena idea agregar todas las posibles combinaciones para mayor robustes (%b, %D, %y)
    if not date_str or not isinstance(date_str, str):
        return ""
    formats = ["%B %d, %Y", "%b %d, %Y", "%m/%d/%Y", "%Y-%m-%d", "%d-%m-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return date_str
