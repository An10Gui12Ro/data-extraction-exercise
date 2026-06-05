"""Unit tests for utility functions. DO NOT MODIFY THIS FILE."""

from src.utils import normalize_name, normalize_date


class TestNormalizeName:
    def test_basic(self):
        assert normalize_name("John Smith") == "John Smith"

    def test_titles(self):
        assert normalize_name("Dr. Jane Doe") == "Jane Doe"

    def test_suffixes(self):
        assert normalize_name("Robert Smith Jr.") == "Robert Smith"

    def test_extra_whitespace(self):
        assert normalize_name("  John   Michael   Smith  ") == "John Michael Smith"

    def test_all_caps(self):
        assert normalize_name("JANE DOE") == "Jane Doe"

    def test_combined(self):
        assert normalize_name("  mr. JOHN  doe esq. ") == "John Doe"


class TestNormalizeDate:
    def test_iso(self):
        assert normalize_date("2023-01-15") == "2023-01-15"

    def test_us_format(self):
        assert normalize_date("01/15/2023") == "2023-01-15"

    def test_long_format(self):
        assert normalize_date("January 15, 2023") == "2023-01-15"

    def test_another_month(self):
        assert normalize_date("March 1, 2022") == "2022-03-01"
