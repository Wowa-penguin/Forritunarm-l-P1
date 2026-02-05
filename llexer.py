"""Imports"""

import sys
from ltoken import LToken


class LLexer:
    """Lexer class"""

    KEY_TOKENS = [
        "if",
        "print",
        ";",
        "end",
        "id",
        "=",
        "+",
        "-",
        "*",
        "int",
        "(",
        ")",
    ]

    ID = 0
    ASSIGN = 1
    SEMICOL = 2
    INT = 3
    PLUS = 4
    MINUS = 5
    MULT = 6
    LPAREN = 7
    RPAREN = 8
    PRINT = 9
    END = 10
    ERROR = 11

    def __init__(self):
        self.lexer = ""
        self.next_char = ""

    def get_next_token(self) -> str:
        """?"""
        while self.next_char != ";":
            self.get_char()
            if self.next_char == " ":
                self.lookup()
            self.lexer += self.next_char

        print(self.lexer)

    def lookup(self):
        """Returns 0 if the lexeme is not a reserved word but token
        code for any reserved word"""
        if self.lexer not in self.KEY_TOKENS:
            return 0
        else:
            pass

    def get_char(self) -> None:
        """
        gets the next character of the input
        puts in variable nextChar
        Determines the character class and puts in variable
        charClass: either Letter or Digit
        """
        self.next_char = sys.stdin.read(1)

    def add_char(self):
        """puts the character in nextChar into lexeme"""
        pass


if __name__ == "__main__":
    t = LLexer()
    t.get_next_token()
