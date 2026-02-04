"""Imports"""

import sys
from ltoken import LToken


class LLexer:
    """
    Lexer class
    - lookup()
        Returns 0 if the lexeme is not a reserved word but token
        code for any reserved word
    - getchar()
        gets the next character of the input
        puts in variable nextChar
        Determines the character class and puts in variable
        charClass: either Letter or Digit
    - addChar()
        puts the character in nextChar into lexeme
    """

    def __init__(self):
        pass

    def get_next_token(self) -> str:
        """?"""
        token = ""
        while True:
            std_input = sys.stdin.read(1)
            if std_input == " ":
                break
            token += std_input
        if token == "END":
            return LToken(token, 10)

        return LToken(token)
