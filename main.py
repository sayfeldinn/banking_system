"""
Simple Banking System - Command Line Interface (main.py)

Runs an interactive loop to deposit, withdraw, check balance, or exit.
Uses the banking functions defined in bank.py and handles errors with try/except.
"""
from __future__ import annotations

import sys
import bank

MENU = (
    "Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, or 'exit' to quit: "
)


def _read_amount(prompt: str) -> float:
    """Prompt the user for an amount and parse it as a float.

    Raises
    ------
    ValueError
        If the input cannot be parsed into a positive number.
    """
    raw = input(prompt).strip()
    # Attempt to parse to float
    amount = float(raw)
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    return amount


def main() -> None:
    print("Simple Banking System. Type 'help' to see options.\n")

    while True:
        action = input(MENU).strip().lower()

        if action in {"exit", "q", "quit"}:
            print("Exiting... Goodbye!")
            break

        if action == "help":
            print("\nOptions:\n  d     Deposit money\n  w     Withdraw money\n  b     Check current balance\n  exit  Quit the program\n")
            continue

        if action == "d":
            try:
                amount = _read_amount("Enter amount to deposit: ")
                new_balance = bank.deposit(amount)
                print(f"Deposited: {amount:.2f}")
                print(f"Current balance: {new_balance:.2f}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            except Exception as e:
                # Fallback for any unexpected runtime error
                print(f"An error occurred: {e}")

        elif action == "w":
            try:
                amount = _read_amount("Enter amount to withdraw: ")
                new_balance = bank.withdraw(amount)
                print(f"Withdrawn: {amount:.2f}")
                print(f"Current balance: {new_balance:.2f}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
            except bank.InsufficientFundsError:
                print("Insufficient funds!")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif action == "b":
            current = bank.check_balance()
            print(f"Current balance: {current:.2f}")

        else:
            print("Unknown option. Type 'help' to see available commands.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")
        try:
            sys.exit(0)
        except SystemExit:
            pass
