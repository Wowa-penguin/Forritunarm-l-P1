"""Imports"""

from ltoken import LToken
from llexer import LLexer

if __name__ == "__main__":

    # test = Hell00Every1
    lexer: LLexer = LLexer()
    curr_token: LToken = LToken("", LToken.ERROR)
    new_line = []

    while curr_token.token_code != LToken.END:
        curr_token = lexer.get_next_token()
        print(curr_token)
        new_line.append(curr_token)

    for x in new_line:
        print(x)
