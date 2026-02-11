"""Imports"""

import sys
from llexer import LLexer
from ltoken import LToken


class LParser:
    """L Parser class
    Statements -> Statement ; Statements | end
    Statement -> id = Expr | print id
    Expr- > Term | Term + Expr | Term - Expr
    Term -> Factor | Factor * Term
    Factor -> int | id | ( Expr )
    """

    def __init__(self, lexer: LLexer):
        self.lexer = lexer
        self.curr_token: LToken = LToken("", LToken.ERROR)
        self.stack: list[LToken] = []  # ? Last-In, First-Out -> append, pop

    def parse(self):
        """?"""
        self.next_token()
        self.statements()

    def next_token(self):
        """get the next token from the lexer"""
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def statements(self):
        """?"""
        while self.curr_token.token_code != LToken.END:
            match self.curr_token.token_code:
                case LToken.ID | LToken.PRINT:
                    self.statement()
                case LToken.SEMICOL:
                    self.next_token()

    def statement(self):
        match self.curr_token.token_code:
            case LToken.ID:
                print(f"PUSH {self.curr_token.token_input}")
                self.next_token()
                if self.curr_token.token_code == LToken.ASSIGN:
                    self.next_token()
                self.expr()
                print("ASSIGN")
            case LToken.PRINT:
                self.next_token()
                if self.curr_token.token_code != LToken.ID:
                    self.error()
                    return
                print(f"PUSH {self.curr_token.token_input}")
                print("PRINT")
                self.next_token()

    def expr(self):
        self.term()
        match self.curr_token.token_code:
            case LToken.PLUS:
                self.next_token()
                self.expr()
                print("ADD")
            case LToken.MINUS:
                self.next_token()
                self.expr()
                print("SUB")
        return

    def term(self):
        self.factor()
        self.next_token()
        match self.curr_token.token_code:
            case LToken.MULT:
                self.next_token()
                self.term()
                print("MULT")
        return

    def factor(self):
        match self.curr_token.token_code:
            case LToken.ID | LToken.INT:
                print(f"PUSH {self.curr_token.token_input}")
                return
            case LToken.LPAREN:
                self.next_token()
                self.expr()
                if self.curr_token.token_code == LToken.RPAREN:
                    return
        return

    def error(self):
        """?"""
        print("Error")
        sys.exit(1)

    def __str__(self):
        for x in self.stack:
            print(x)
        return ""


if __name__ == "__main__":
    test_lexer: LLexer = LLexer()
    parser: LParser = LParser(test_lexer)
    parser.parse()
    print(parser)
