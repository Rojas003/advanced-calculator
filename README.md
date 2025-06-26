# Advanced Calculator 🧮

An advanced, modular, and extensible command-line calculator built in Python, designed with software engineering principles and design patterns.

---

##  Features

- **REPL Interface**: Responsive command-line interface for user interaction.
- **Arithmetic Operations**: Supports `+`, `-`, `*`, `/`.
- **Design Patterns**:
  - **Strategy**: Implements operations as interchangeable strategies.
  - **Observer**: Logs results to a history file (`history.csv`).
  - **Memento**: Supports undo functionality for previous calculations.
- **Configuration Management**: Uses `.env` and `dotenv` to load settings (e.g., CSV filename).
- **History Logging**: Tracks all calculations via `pandas`.
- **Robust Error Handling**: LBYL and EAFP patterns used throughout.
- **Unit Testing**: 100% test coverage using `pytest`.
- **CI/CD**: Integrated with GitHub Actions.

---

##  Project Structure
advanced-calculator/
├── app/
│   ├── calculator/              # Entry point module
│   ├── calculation/             # Calculation logic
│   ├── operation/               # Strategy + Factory for math ops
│   ├── observer/                # Observer pattern (CSV logger)
│   ├── memento/                 # Undo/redo infrastructure
│   ├── calculator_repl.py       # REPL loop and input parsing
│   ├── config.py                # Loads env vars
│   └── __init__.py
├── tests/                       # All test modules
├── .env                         # App settings
├── history.csv                  # Auto-generated log
├── main.py                      # Application entry point
├── requirements.txt             # Dependencies
└── README.md                    # You're reading it


---

## ⚙️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Rojas003/advanced-calculator.git
cd advanced-calculator

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt

APP_MODE=development
HISTORY_FILE=history.csv

pytest --cov=app

python main.py


---

###  Push your project to GitHub

1. **Initialize git (if not already):**

```bash
git init
git commit -m "Add full README with usage, design patterns, and features"

git add .
git commit -m "Final project complete with README"

git remote add origin https://github.com/Rojas003/advanced-calculator.git

git push -u origin main

Usage Notes
Type calculations like:
5 + 3, 10 / 2, 2 ** 3, 100 % 3, 9 root 2

Meta-commands:

exit – quit

history – print history

undo – undo last operation

redo – redo last undone operation

save – manually save current session