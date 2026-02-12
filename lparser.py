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

    def parse(self):
        """Main call to start the parser"""
        self.next_token()
        self.statements()

    def next_token(self):
        """Get the next token from the lexer"""
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error("Syntax error")

    def statements(self):
        """Statements -> Statement ; Statements | end"""
        while self.curr_token.token_code != LToken.END:
            match self.curr_token.token_code:
                case LToken.ID | LToken.PRINT:
                    self.statement()
                case LToken.SEMICOL:
                    self.next_token()
                case LToken.ERROR:
                    self.error("Syntax error")

    def statement(self):
        """Statement -> id = Expr | print id"""
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
                    error_msg = [
                        key
                        for key, value in self.lexer.KEY_TOKENS.items()
                        if value == self.curr_token.token_code
                    ]
                    self.error(f"Syntax error print a variable not {error_msg[0]}")
                    return
                print(f"PUSH {self.curr_token.token_input}")
                print("PRINT")
                self.next_token()

    def expr(self):
        """Expr -> Term | Term + Expr | Term - Expr"""
        self.term()
        match self.curr_token.token_code:
            case LToken.PLUS:
                self.next_token()
                self.expr()
                print("ADD")
                return
            case LToken.MINUS:
                self.next_token()
                self.expr()
                print("SUB")
                return
            case _ if self.curr_token.token_code not in self.lexer.KEY_TOKENS.values():
                self.error("Syntax error")
        return

    def term(self):
        """Term -> Factor | Factor * Term"""
        self.factor()
        self.next_token()
        match self.curr_token.token_code:
            case LToken.MULT:
                self.next_token()
                self.term()
                print("MULT")
        return

    def factor(self):
        """Factor -> int | id | ( Expr )"""
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

    def error(self, msg: str):
        """Print error msg and exit program"""
        print(msg)
        sys.exit(1)


if __name__ == "__main__":
    test_lexer: LLexer = LLexer()
    parser: LParser = LParser(test_lexer)
    parser.parse()
    print(parser)
