"""Imports"""


class LToken:
    """
    L token class
    The intege constants are the following:
    { ID, ASSIGN, SEMICOL, INT, PLUS, MINUS, MULT, LPAREN, RPAREN, PRINT, END, ERROR}
    INT = [0-9]+
    ID = [A-Za-z]+
    END = end
    PRINT = print
    Tokens/terminals are:
    ; end id = print + - * int ( )
    """

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

    # * reserved words
    def __init__(self, token_input, token=-1):
        self.token_input = token_input
        self.token_code = token

    def __str__(self) -> str:
        return f"{self.token_input} {self.token_code}"
