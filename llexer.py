"""Imports"""

import sys
from ltoken import LToken


class LLexer:
    """Lexer class"""

    KEY_TOKENS = {
        "=": 1,
        ";": 2,
        "+": 4,
        "-": 5,
        "*": 6,
        "(": 7,
        ")": 8,
        "print": 9,
        "end": 10,
    }

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
        self.key_chars: list = []
        for key in self.KEY_TOKENS.keys():
            self.key_chars.append(key)
        self.key_chars.append("\n")

    def get_next_token(self) -> LToken:
        """?"""
        self.lexer = ""

        if self.next_char in self.key_chars:
            token: LToken = self.make_key_token()
            self.next_char = ""
            return token

        if self.next_char == "\n":
            return LToken(self.next_char, self.ID)

        while True:
            self.get_char()
            if self.next_char == " ":
                self.get_char()

            if self.next_char.isalpha() or self.next_char.isdigit():
                self.lexer += self.next_char

            if not self.next_char.isalpha() or self.next_char.isdigit():
                token: LToken = self.make_token()
                return token

    def make_token(self):
        if self.lexer == "end":
            return LToken(self.lexer.strip(), self.END)

        if self.lexer.isdigit():
            return LToken(self.lexer.strip(), self.INT)

        if self.lexer.isalpha():
            return LToken(self.lexer.strip(), self.ID)

    def make_key_token(self):
        if self.next_char in self.key_chars:
            return LToken(self.next_char.strip(), self.KEY_TOKENS[self.next_char])

    def get_char(self) -> None:
        """
        gets the next character of the input
        puts in variable nextChar
        Determines the character class and puts in variable
        charClass: either Letter or Digit
        """
        self.next_char = sys.stdin.read(1)


if __name__ == "__main__":
    t = LLexer()
    k = t.get_next_token()
    print(k)
