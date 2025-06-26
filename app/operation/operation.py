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
def power(a, b):
    return a ** b

def root(a, b):
    if b == 0:
        raise ValueError("Root exponent cannot be zero.")
    return a ** (1 / b)

def modulus(a, b):
    return a % b

def int_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b

def percent(a, b):
    if b == 0:
        raise ValueError("Cannot calculate percentage with divisor zero.")
    return (a / b) * 100

def abs_diff(a, b):
    return abs(a - b)
