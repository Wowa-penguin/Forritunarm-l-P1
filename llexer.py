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

    def __init__(self):
        self.lexer = ""
        self.next_char = ""
        self.key_chars: list = []
        for key in self.KEY_TOKENS.keys():
            self.key_chars.append(key)
        self.key_chars.append("\n")

    def get_next_token(self) -> LToken:
        """Return a new Token from std in"""
        self.lexer = ""
        while self.check_space():
            self.get_char()

        if self.next_char in self.key_chars or self.next_char == "\n":
            return self.is_key_token()

        if not self.next_char.isdigit() and not self.next_char.isalpha():
            self.get_char()

        return self.is_var_token()

    def is_key_token(self) -> LToken:
        """if next_char is a key value make a new token"""
        self.lexer += self.next_char
        if self.next_char in self.key_chars:
            self.get_char()
            return LToken(self.lexer.strip(), self.KEY_TOKENS[self.lexer])

        if self.next_char == "\n":
            self.get_char()
            return LToken(self.lexer, LToken.ID)

        return None

    def is_var_token(self) -> LToken:
        """Find all char to make a int or string value"""
        while True:
            if self.next_char.isalpha() or self.next_char.isdigit():
                self.lexer += self.next_char

            if not self.next_char.isalpha() and not self.next_char.isdigit():
                token: LToken = self.make_token()
                return token
            self.get_char()

    def make_token(self) -> LToken:
        """Make a token for a long strign and check if value is end og print"""
        if self.lexer == "end":
            return LToken(self.lexer.strip(), LToken.END)

        if self.lexer == "print":
            return LToken(self.lexer.strip(), LToken.PRINT)

        if self.lexer.isdigit():
            return LToken(self.lexer.strip(), LToken.INT)

        return LToken(self.lexer.strip(), LToken.ID)

    def get_char(self) -> None:
        """
        gets the next character of the input
        puts in variable nextChar
        Determines the character class and puts in variable
        charClass: either Letter or Digit
        """
        self.next_char = sys.stdin.read(1)

    def check_space(self) -> bool:
        """check if next char has space"""
        return self.next_char.isspace()
