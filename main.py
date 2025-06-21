from app import config
from app.calculator_repl import start_repl

def main():
    print("MAIN.PY IS RUNNING")
    print("App Mode:", config.APP_MODE)
    print("History File:", config.HISTORY_FILE)
    start_repl()  # This line starts the calculator loop

if __name__ == "__main__":
    main()
