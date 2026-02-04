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
    """

    KEY_TOKENS = [
        "if",
        "print",
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
        if token == -1:
            self.set_token_code()

    def set_token_code(self) -> None:
        """set the token code from the input"""
        if self.token_input not in self.KEY_TOKENS:
            self.token_code = self.ASSIGN
            return

        match self.token_input:
            case "int":
                self.token_code = self.INT
            case "print":
                self.token_code = self.PRINT
            case "+":
                self.token_code = self.PLUS
            case "-":
                self.token_code = self.MINUS
            case "*":
                self.token_code = self.MULT
            case ";":
                self.token_code = self.SEMICOL
            case "\n":
                self.token_code = self.END

    def __str__(self) -> str:
        return self.token_input
