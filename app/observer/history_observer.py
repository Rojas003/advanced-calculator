# app/observer/history_observer.py

import csv
from app import config
from app.observer.observer import Observer

class HistoryObserver(Observer):
    def update(self, expression: str, result: float):
        with open(config.HISTORY_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([expression, result])
