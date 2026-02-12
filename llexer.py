"""Imports"""

import sys
from ltoken import LToken


class LLexer:
    """Lexer class"""

    KEY_TOKENS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    _SINGLE_CHAR_TOKENS = {
        "=": LToken.ASSIGN,
        ";": LToken.SEMICOL,
        "+": LToken.PLUS,
        "-": LToken.MINUS,
        "*": LToken.MULT,
        "(": LToken.LPAREN,
        ")": LToken.RPAREN,
    }

    def __init__(self):
        self.lexer = ""
        self.next_char = ""

    def get_next_token(self) -> LToken:
        """Return a new Token from stdin."""

        if self.next_char == "":
            self.get_char()

        while self.next_char != "" and self.next_char.isspace():
            self.get_char()

        if self.next_char == "":
            return LToken("", LToken.ERROR)

        if self.next_char in self._SINGLE_CHAR_TOKENS:
            ch = self.next_char
            self.get_char()
            return LToken(ch, self._SINGLE_CHAR_TOKENS[ch])

        if self.next_char.isalpha() or self.next_char.isdigit():
            self.lexer = ""
            while self.next_char != "" and (
                self.next_char.isalpha() or self.next_char.isdigit()
            ):
                self.lexer += self.next_char
                self.get_char()
            return self.make_token()

        bad = self.next_char
        self.get_char()
        return LToken(bad, LToken.ERROR)

    def make_token(self) -> LToken:
        """Make a token for a collected lexeme."""
        if self.lexer == "end":
            return LToken(self.lexer, LToken.END)
        if self.lexer == "print":
            return LToken(self.lexer, LToken.PRINT)
        if self.lexer.isdigit():
            return LToken(self.lexer, LToken.INT)
        return LToken(self.lexer, LToken.ID)

    def get_char(self) -> None:
        """Read one character from stdin into self.next_char."""
        self.next_char = sys.stdin.read(1)
