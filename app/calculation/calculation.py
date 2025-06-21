class Calculation:
    def __init__(self, operand1, operand2, operation_func):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operation_func = operation_func
        self.result = self.operation_func(self.operand1, self.operand2)

    def __str__(self):
        return f"{self.operand1} {self.operation_func.__name__} {self.operand2} = {self.result}"
# app/calculation/calculation.py

class Calculation:
    def __init__(self, a, b, strategy):
        self.a = a
        self.b = b
        self.strategy = strategy  # This will be an instance of a Strategy class

    def execute(self):
        return self.strategy.execute(self.a, self.b)
