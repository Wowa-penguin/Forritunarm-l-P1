"""Imports"""

import sys
from llexer import LLexer
from ltoken import LToken


class LParser:
    """L Parser class
    PUSH op ADD SUB MULT ASSIGN PRINT pushes the operand op onto the stack
    ADD     - pops the two top elements from the stack, adds their values
            - and pushes the result back onto the stack
    SUB     - pops the two top elements from the stack, subtracts the first
            - value retrieved from the second value,
            - and pushes the result back onto the stack
    MULT    - pops the two top elements from the stack, multiplies their
            - values and pushes the result back onto the stack
    ASSIGN  - pops the two top elements from the stack, assigns the first
            - element (a value) to the second element (a variable)
    PRINT   - prints the value currently on top of the stack
    """

    def __init__(self, lexer: LLexer):
        self.lexer = lexer
        self.curr_token: LToken = LToken("", LToken.ERROR)
        self.stack = []  # ? Last-In, First-Out -> append, pop
        self.ops = []

    def parse(self):
        """?"""
        while self.curr_token.token_code != LToken.END:
            self.next_token()
            if self.curr_token.token_code == LToken.SEMICOL:

                self.statements()
                print("\n")

    def next_token(self):
        """?"""
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()
        else:
            self.stack.append(self.curr_token)

    def statements(self):
        """?"""
        while True:
            next_token: LToken = self.stack.pop()
            match next_token.token_code:
                case LToken.ASSIGN:
                    # ASSIGN
                    pass

    def error(self):
        """?"""
        print("Error")
        sys.exit(1)


if __name__ == "__main__":
    test_lexer: LLexer = LLexer()
    parser: LParser = LParser(test_lexer)
    parser.parse()
