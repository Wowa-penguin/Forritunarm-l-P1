"""Imports"""

from ltoken import LToken
from llexer import LLexer

if __name__ == "__main__":

    # test = Hell00Every1
    lexer: LLexer = LLexer()
    curr_token: LToken = LToken("", LToken.ERROR)

    while curr_token.token_code != LToken.END:
        curr_token = lexer.get_next_token()
        print(curr_token)
