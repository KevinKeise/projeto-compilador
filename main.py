from antlr4 import *
from gen.MyFinalGrammar import MyFinalGrammar
from gen.finalgrammarLexer import finalgrammarLexer
from gen.finalgrammarParser import finalgrammarParser

if __name__ == '__main__':
    exp = 'real var111 = 2.4,var113=56.34; def main(){int ai = 2;print("ao","asd");m = 34+var;}'
    data = InputStream(exp)

    lexer = finalgrammarLexer(data)
    tokens = CommonTokenStream(lexer)

    parser = finalgrammarParser(tokens)
    tree = parser.programa()

    listener = MyFinalGrammar()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
