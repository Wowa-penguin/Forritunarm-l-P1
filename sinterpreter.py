"""Imports"""

import sys
from typing import Union


class SInterpreter:
    """SInterpreter"""

    def __init__(self):
        self.stack = []  # ? Last-In, First-Out -> append, pop
        self.var = {}

    def in_var(self, value):
        """Check if a instans of a var is in dict of var"""
        if value in self.var:
            return self.var[value]
        return value

    def add(self):
        """ADD
        -- pops the two top elements from the stack, adds their values
        -- and pushes the result back onto the stack
        """
        value_1 = self.stack.pop()
        value_2 = self.stack.pop()

        value_1 = self.in_var(value_1)
        value_2 = self.in_var(value_2)

        try:
            self.stack.append(int(value_1) + int(value_2))
        except ValueError:
            print("Error")
            sys.exit(1)

    def sub(self):
        """SUB
        -- pops the two top elements from the stack, subtracts the first
        -- value retrieved from the second value,
        -- and pushes the result back onto the stack
        """
        value_1 = self.stack.pop()
        value_2 = self.stack.pop()
        value_1 = self.in_var(value_1)
        value_2 = self.in_var(value_2)
        self.stack.append(int(value_2) - int(value_1))

    def push(self, value: Union[int, str]):
        """PUSH
        -- pushes the operand op onto the stack
        """
        value = value.strip()
        if value.isdigit():
            self.stack.append(int(value))
        else:
            self.stack.append(value)

    def mult(self):
        """MULT
        -- pops the two top elements from the stack, multiplies their
        -- values and pushes the result back onto the stack
        """
        value_1 = self.stack.pop()
        value_2 = self.stack.pop()
        value_1 = self.in_var(value_1)
        value_2 = self.in_var(value_2)
        self.stack.append(int(value_1) * int(value_2))

    def assign(self):
        """ASSIGN
        -- pops the two top elements from the stack, assigns the first
        -- element (a value) to the second element (a variable)
        """
        value = self.stack.pop()
        var = self.stack.pop()
        self.var[var] = value

    def print_stack(self):
        """PRINT
        -- prints the value currently on top of the stack
        """
        value = self.stack.pop()
        if value in self.var:
            value = self.var[value]
        print(value)

    def cycle(self):
        """Main loop"""
        var = ""
        while True:
            var = sys.stdin.readline()
            var = var.replace("\n", "").split(" ")
            if var[0] == "":
                break
            op = var[0]
            if op == "PUSH":
                self.push(var[1])
            elif op == "SUB":
                self.sub()
            elif op == "MULT":
                self.mult()
            elif op == "ASSIGN":
                self.assign()
            elif op == "ADD":
                self.add()
            elif op == "PRINT":
                self.print_stack()


if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()
