"""Imports"""

import sys
from llexer import LLexer
from ltoken import LToken


class LParser:
    """L Parser class
    PUSH op ADD SUB MULT ASSIGN PRINT pushes the operand op onto the stack
    ADD     - pops the two top elements from the stack, adds their values
            - and pushes the result back onto the stack
    SUB     - pops the two top elements from the stack, subtracts the first
            - value retrieved from the second value,
            - and pushes the result back onto the stack
    MULT    - pops the two top elements from the stack, multiplies their
            - values and pushes the result back onto the stack
    ASSIGN  - pops the two top elements from the stack, assigns the first
            - element (a value) to the second element (a variable)
    PRINT   - prints the value currently on top of the stack
    """

    def __init__(self, lexer: LLexer):
        self.lexer = lexer
        self.curr_token: LToken = LToken("", LToken.ERROR)
        self.stack: list[LToken] = []  # ? Last-In, First-Out -> append, pop
        self.var_list: list[LToken] = []
        self.ops_list: list[LToken] = []

    def parse(self):
        """?"""
        while self.curr_token.token_code != LToken.END:
            self.next_token()
            self.statements()

    def next_token(self):
        """get the next token from the lexer"""
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def statements(self):
        """?"""
        match self.curr_token.token_code:
            case LToken.ID | LToken.INT:
                self.var_list.append(self.curr_token)
            case (
                LToken.ASSIGN
                | LToken.PLUS
                | LToken.MINUS
                | LToken.MULT
                | LToken.PRINT
                | LToken.LPAREN
                | LToken.RPAREN
            ):
                self.ops_list.append(self.curr_token)
            case LToken.SEMICOL:
                self.add_to_stack()

    def add_to_stack(self):
        """Add tokens to the stack in correct order"""

        for var_token in self.var_list:
            self.stack.append(var_token)
        self.var_list = []

        is_paren, left_index, right_index = self.check_for_paren()
        if is_paren:
            print(left_index, right_index)
            print(len(self.ops_list))
            for x in self.ops_list[left_index + 1 : right_index]:
                self.stack.append(x)

            self.ops_list.remove(self.ops_list[left_index])
            self.ops_list.remove(self.ops_list[right_index - 1])

        for op_token in self.ops_list:
            print(op_token)
            self.stack.append(op_token)

        self.ops_list = []

    def check_for_paren(self):
        left_index = 0
        right_index = 0
        is_paren = False

        for index, op_token in enumerate(self.ops_list):
            if LToken.LPAREN == op_token.token_code:
                is_paren = True
                left_index = index
            if LToken.RPAREN == op_token.token_code:
                right_index = index

        return is_paren, left_index, right_index

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
