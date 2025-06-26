import csv
from app import config
from app.observer.observer import Observer

class HistoryObserver(Observer):
    def __init__(self, history_file: str):
        self.history_file = history_file

    def update(self, expression: str, result: float):
        with open(self.history_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([expression, result])