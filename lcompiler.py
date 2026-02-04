"""Imports"""

from llexer import LLexer
from lparser import LParser

if __name__ == "__main__":
    lexer: LLexer = LLexer()
    parser: LParser = LParser(lexer)
    parser.parse()
