import sys


class SInterpreter:
    """SInterpreter"""

    def __init__(self):
        self.stack = []  # ? Last-In, First-Out -> append, pop
        self.var = {}

    def add(self):
        """ADD
        -- pops the two top elements from the stack, adds their values
        -- and pushes the result back onto the stack
        """
        value_1 = self.stack.pop()
        value_2 = self.stack.pop()
        if value_1 in self.var.keys():
            value_1 = self.var[value_1]
        if value_2 in self.var.keys():
            value_2 = self.var[value_2]
        try:
            self.stack.append(int(value_1) + int(value_2))
        except TypeError:
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
        if value_1 in self.var.keys():
            value_1 = self.var[value_1]
        if value_2 in self.var.keys():
            value_2 = self.var[value_2]
        self.stack.append(int(value_2) - int(value_1))

    def push(self, value: int | str):
        """PUSH
        -- pushes the operand op onto the stack
        """
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
        if value_1 in self.var.keys():
            value_1 = self.var[value_1]
        if value_2 in self.var.keys():
            value_2 = self.var[value_2]
        self.stack.append(int(value_1) * int(value_2))

    def assign(self):
        """ASSIGN
        -- pops the two top elements from the stack, assigns the first
        -- element (a value) to the second element (a variable)
        """
        value = self.stack.pop()
        var = self.stack.pop()
        self.var[var] = value

    def print(self):
        """PRINT
        -- prints the value currently on top of the stack
        """
        value = self.stack.pop()
        if value in self.var.keys():
            value = self.var[value]
        print(value)

    def cycle(self):
        var = ""
        while True:
            var = sys.stdin.readline()
            var = var.replace("\n", "").split(" ")
            if var[0] == "":
                break
            match var[0]:
                case "PUSH":
                    self.push(var[1])
                case "SUB":
                    self.sub()
                case "MULT":
                    self.mult()
                case "ASSIGN":
                    self.assign()
                case "ADD":
                    self.add()
                case "PRINT":
                    self.print()


if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()
