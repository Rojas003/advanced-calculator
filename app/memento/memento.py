# app/memento/memento.py

class Memento:
    def __init__(self, expression: str, result: float):
        self.expression = expression
        self.result = result

    def get_expression(self):
        return self.expression

    def get_result(self):
        return self.result