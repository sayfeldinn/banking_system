"""
Utility helpers for the Simple Banking System (utils.py)

These helpers are optional. They provide basic input parsing/validation
so the main CLI stays clean. You can import and use them in main.py.
"""
from __future__ import annotations


def parse_positive_amount(text: str) -> float:
    """Parse *text* into a positive float.

    Parameters
    ----------
    text : str
        Raw user input representing a numeric amount.

    Returns
    -------
    float
        Parsed positive number.

    Raises
    ------
    ValueError
        If the text cannot be parsed as a number or is <= 0.
    """
    amount = float(text)
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    return amount


def read_positive_amount(prompt: str = "Enter amount: ") -> float:
    """Prompt the user to enter a positive float and return it.

    This wraps input() + parse_positive_amount() and lets callers
    just handle ValueError in one place.
    """
    raw = input(prompt).strip()
    return parse_positive_amount(raw)
