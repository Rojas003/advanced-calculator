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
│ ├── calculation/
│ │ └── calculation.py
│ ├── calculator/
│ │ └── init.py
│ ├── memento/
│ │ ├── memento.py
│ │ └── caretaker.py
│ ├── observer/
│ │ ├── observer.py
│ │ ├── subject.py
│ │ └── history_observer.py
│ ├── operation/
│ │ ├── init.py
│ │ └── operation.py
│ ├── config.py
│ └── calculator_repl.py
├── tests/
│ └── test_*.py
├── .env
├── history.csv
├── main.py
└── README.md


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
