"""Imports"""

from ltoken import LToken
from llexer import LLexer

if __name__ == "__main__":
    lexer: LLexer = LLexer()
    curr_token: LToken = LToken("", LToken.ERROR)
    new_line = []

    while curr_token.token_code != LToken.END:
        curr_token = lexer.get_next_token()
        if curr_token.token_code != LToken.SEMICOL:
            new_line.append(curr_token)
        else:
            break
        for t in new_line:
            print(t)
    print(new_line)
