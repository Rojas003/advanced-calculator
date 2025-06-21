from app.observer.subject import Subject
from app.observer.history_observer import HistoryObserver
from app.calculation.calculation import Calculation
from app.operation.operation import AddStrategy, SubtractStrategy, MultiplyStrategy, DivideStrategy
from app.memento.caretaker import Caretaker
from app.memento.memento import Memento


def start_repl():
    # Step 1: Setup Observer Pattern
    subject = Subject()
    history_observer = HistoryObserver()
    subject.attach(history_observer)

    # Step 2: Setup Memento (Undo/Redo)
    caretaker = Caretaker()

    print("History File: history.csv")
    print("Welcome to the Advanced Calculator! Type 'exit' to quit, or 'undo' to revert the last step, or 'redo' to reapply.")

    while True:
        user_input = input("Enter a calculation (e.g. 2 + 2): ")

        if user_input.lower() in ["exit", "q"]:
            print("Goodbye!")
            break

        if user_input.lower() == "undo":
            memento = caretaker.undo()
            if memento:
                print(f"Undo → {memento.expression} = {memento.result}")
            else:
                print("Nothing to undo.")
            continue

        if user_input.lower() == "redo":
            memento = caretaker.redo()
            if memento:
                print(f"Redo → {memento.expression} = {memento.result}")
            else:
                print("Nothing to redo.")
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid input format. Please use format like '2 + 2'.")
            continue

        try:
            value1 = float(parts[0])
            operator = parts[1]
            value2 = float(parts[2])

            if operator == "+":
                strategy = AddStrategy()
            elif operator == "-":
                strategy = SubtractStrategy()
            elif operator == "*":
                strategy = MultiplyStrategy()
            elif operator == "/":
                strategy = DivideStrategy()
            else:
                print("Unsupported operator. Use +, -, *, or /.")
                continue

            calc = Calculation(value1, value2, strategy)
            result = calc.execute()

            # Save current operation as a Memento
            expression = f"{value1} {operator} {value2}"
            memento = Memento(expression, result)
            caretaker.add_memento(memento)

            # Notify observers
            subject.notify(expression, result)

            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")
