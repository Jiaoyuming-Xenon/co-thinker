"""Application package for Co-Thinker."""

from app.parser import (
    DocxParser,
    DocumentParser,
    PARSER_REGISTRY,
    PDFParser,
    PPTXParser,
    TEXT_EXTENSIONS,
    TextParser,
)

__all__ = [
    "DocumentParser",
    "TextParser",
    "PDFParser",
    "DocxParser",
    "PPTXParser",
    "PARSER_REGISTRY",
    "TEXT_EXTENSIONS",
]
