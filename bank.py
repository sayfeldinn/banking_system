"""
Simple Banking System Module (bank.py)

This module manages the core banking logic for a single in-memory account.
It exposes three primary functions required by the assignment:
  - deposit(amount)
  - withdraw(amount)
  - check_balance()

Notes
-----
* Amounts must be positive numbers.
* Withdrawal checks for sufficient funds and raises InsufficientFundsError if not enough balance.
* Balance is stored in-memory as a module-level variable.
"""
from __future__ import annotations

from typing import Final

__all__ = [
    "InsufficientFundsError",
    "deposit",
    "withdraw",
    "check_balance",
]


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is attempted with insufficient balance."""


# Internal account state (single-user for this simple system)
_BALANCE: float = 0.0

# Optional: Minimal precision handling (formatting/rounding to 2 decimals)
# We keep full float precision internally but round returns for user display consistency.
_CURRENCY_DECIMALS: Final[int] = 2


def _ensure_positive(amount: float) -> None:
    """Validate that *amount* is a positive number.

    Raises
    ------
    ValueError
        If amount is not a number or not strictly positive.
    """
    # Type/NaN/Inf guards (in case callers bypass input validation)
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number.")
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")


def deposit(amount: float) -> float:
    """Add *amount* to the current balance and return the new balance.

    Parameters
    ----------
    amount : float
        The amount to deposit. Must be > 0.

    Returns
    -------
    float
        The updated balance (rounded to 2 decimals for display).

    Raises
    ------
    ValueError
        If *amount* is not a positive number.
    """
    global _BALANCE
    _ensure_positive(amount)
    _BALANCE += float(amount)
    return round(_BALANCE, _CURRENCY_DECIMALS)


def withdraw(amount: float) -> float:
    """Subtract *amount* from the current balance and return the new balance.

    Parameters
    ----------
    amount : float
        The amount to withdraw. Must be > 0 and <= current balance.

    Returns
    -------
    float
        The updated balance (rounded to 2 decimals for display).

    Raises
    ------
    ValueError
        If *amount* is not a positive number.
    InsufficientFundsError
        If *amount* exceeds the current balance.
    """
    global _BALANCE
    _ensure_positive(amount)

    if amount > _BALANCE:
        raise InsufficientFundsError("Insufficient funds!")

    _BALANCE -= float(amount)
    return round(_BALANCE, _CURRENCY_DECIMALS)


def check_balance() -> float:
    """Return the current balance (rounded to 2 decimals)."""
    return round(_BALANCE, _CURRENCY_DECIMALS)


# --- Optional helpers (not required, but useful for testing) ---

def _reset_balance(value: float = 0.0) -> None:
    """Reset the internal balance (for tests). Not intended for production use."""
    global _BALANCE
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError("Reset value must be a non-negative number.")
    _BALANCE = float(value)
