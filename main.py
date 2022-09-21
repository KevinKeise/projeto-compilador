from antlr4 import *
from gen.MyFinalGrammar import MyFinalGrammar
from gen.finalgrammarLexer import finalgrammarLexer
from gen.finalgrammarParser import finalgrammarParser


def le_arquivo(nome):
    with open(nome) as file:
        data = file.read()
        file.close()
        return data


if __name__ == '__main__':
    d = le_arquivo("code.py")
    exp = d
    data = InputStream(exp)

    lexer = finalgrammarLexer(data)
    tokens = CommonTokenStream(lexer)

    parser = finalgrammarParser(tokens)
    tree = parser.programa()

    listener = MyFinalGrammar()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
