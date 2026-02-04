"""Imports"""

from llexer import LLexer
from ltoken import LToken


class LParser:
    """L Parser class"""

    def __init__(self, lexer: LLexer):
        self.lexer = lexer
        self.curr_token: LToken = LToken("", LToken.ERROR)

    def parse(self):
        self.next_token()
        self.statements()
        print()

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def statements(self):
        pass

    def error(self):
        pass
