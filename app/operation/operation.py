# app/operation/operation.py

from abc import ABC, abstractmethod

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(OperationStrategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(OperationStrategy):
    def execute(self, a, b):
        return a - b

class MultiplyStrategy(OperationStrategy):
    def execute(self, a, b):
        return a * b

class DivideStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
