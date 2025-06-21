from typing import List
from app.observer.observer import Observer  # ✅ This line fixes the error

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, expression: str, result: float):
        for observer in self._observers:
            observer.update(expression, result)
