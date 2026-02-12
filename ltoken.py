"""Imports"""


class LToken:
    """
    L token class
    The intege constants are the following:
    { ID, ASSIGN, SEMICOL, INT, PLUS, MINUS, MULT, LPAREN, RPAREN, PRINT, END, ERROR}
    INT = [0-9]+
    ID = [A-Za-z]+
    Tokens/terminals are:
        ; end id = print + - * int ( )
    """

    TOKENS = {
        0: "ID",
        1: "ASSIGN",
        2: "SEMICOL",
        3: "INT",
        4: "PLUS",
        5: "MINUS",
        6: "MULT",
        7: "LPAREN",
        8: "RPAREN",
        9: "PRINT",
        10: "END",
        11: "ERROR",
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

    def __init__(self, lexeme, token=-1):
        self.lexeme = lexeme
        self.token_code = token

    def __str__(self) -> str:
        return f"{self.TOKENS[self.token_code]} {self.lexeme} "
