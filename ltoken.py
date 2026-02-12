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

    def __str__(self):
        return f"LToken({self.token_code}, '{self.lexeme}')"

    def __repr__(self):
        return self.__str__()
