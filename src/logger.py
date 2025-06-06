"""Shared logging utilities for TrendSpire."""

from __future__ import annotations

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


def get_trendspire_logger(name: str) -> logging.Logger:
    """Return a logger configured for TrendSpire."""
    return logging.getLogger(name)
