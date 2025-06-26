# app/calculator_repl.py
"""
Interactive REPL for the Advanced Calculator.

Features
--------
* Factory pattern to obtain the correct operation function.
* Memento pattern (Caretaker + Memento) for undo / redo.
* Observer pattern to log each calculation automatically.
* Robust input validation & error handling.
"""

from __future__ import annotations

from typing import Optional
from app import config
from app.operation.factory import get_operation          # Factory
from app.calculation.calculation import Calculation
from app.memento.caretaker import Caretaker              # Memento caretaker
from app.memento.memento import Memento
from app.observer.subject import Subject                 # Observer subject
from app.observer.history_observer import HistoryObserver

# --------------------------------------------------------------------------- #
# Helper tables for user prompts
# --------------------------------------------------------------------------- #

_PROMPT = (
    "Enter a calculation (e.g. 2 + 2) or one of the commands:\n"
    "  history   – show history (in-memory list)\n"
    "  undo      – undo last calculation\n"
    "  redo      – redo an undone calculation\n"
    "  save      – write history to CSV (manual save)\n"
    "  exit      – quit\n"
    "> "
)

# --------------------------------------------------------------------------- #
# Main REPL
# --------------------------------------------------------------------------- #


def start_repl() -> None:
    """Run the calculator Read-Eval-Print Loop."""
    # Memento infrastructure
    caretaker = Caretaker()

    # Observer infrastructure
    subject = Subject()
    history_observer = HistoryObserver(config.HISTORY_FILE)
    subject.attach(history_observer)

    print("Welcome to the Advanced Calculator! Type 'exit' to quit, "
          "or 'undo' / 'redo' / 'history' / 'save'.")

    # --- REPL loop --------------------------------------------------------- #
    while True:
        user_input = input(_PROMPT).strip()

        # ------------------ meta-commands ---------------------------------- #
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if user_input.lower() == "history":
            for idx, mem in enumerate(caretaker.history, 1):
                print(f"{idx:>3}: {mem.get_expression()} = {mem.get_result()}")
            continue

        if user_input.lower() == "undo":
            mem = caretaker.undo()
            if mem:
                print(f"⤺  Undid: {mem.get_expression()} = {mem.get_result()}")
            else:
                print("Nothing to undo.")
            continue

        if user_input.lower() == "redo":
            mem = caretaker.redo()
            if mem:
                print(f"⤻  Redid: {mem.get_expression()} = {mem.get_result()}")
            else:
                print("Nothing to redo.")
            continue

        if user_input.lower() == "save":
            caretaker.save_history()          # caretaker handles CSV write
            print("History saved manually.")
            continue

        # ------------------ parse a calculation --------------------------- #
        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid format; please enter:  <number> <operator> <number>")
            continue

        try:
            a = float(parts[0])
            op_symbol = parts[1]
            b = float(parts[2])

            # Factory → operation function
            operation_func = get_operation(op_symbol)

            # Perform calculation
            calc = Calculation(a, b, operation_func)
            result = calc.execute()

            # Persist using Memento pattern
            expr = f"{a} {op_symbol} {b}"
            caretaker.add_memento(Memento(expr, result))

            # Notify observers (logs to CSV automatically)
            subject.notify(expr, result)

            print(f"Result: {result}")

        except ValueError as ve:
            # Typical numeric / zero-division errors
            print(f"Value error: {ve}")

        except KeyError:
            print(f"Unknown operation: '{op_symbol}'")

        except Exception as ex:               # catch-all for unexpected issues
            print(f"Unexpected error: {ex}")


# --------------------------------------------------------------------------- #
# Script entry point
# --------------------------------------------------------------------------- #

if __name__ == "__main__":
    start_repl()
