# app/memento/caretaker.py

from .memento import Memento

class Caretaker:
    def __init__(self):
        self._history = []

    def add_memento(self, memento: Memento):
        self._history.append(memento)

    def undo(self) -> Memento:
        if self._history:
            return self._history.pop()
        else:
            return None
