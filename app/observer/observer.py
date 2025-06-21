# app/observer/observer.py

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, expression: str, result: float):
        pass
