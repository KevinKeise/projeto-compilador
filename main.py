from antlr4 import *
from gen.MyFinalGrammar import MyFinalGrammar
from gen.finalgrammarLexer import finalgrammarLexer
from gen.finalgrammarParser import finalgrammarParser

if __name__ == '__main__':
    exp = 'real var111 = 2.4,var113=56.8;real va;def v() bool {bool jk;return 3+5;}def vic(int asdo, real c) int {int jk;v();return 3+5;} def main(){real ai = 2.9;print("ao","asd");m = 34;}'
    data = InputStream(exp)

    lexer = finalgrammarLexer(data)
    tokens = CommonTokenStream(lexer)

    parser = finalgrammarParser(tokens)
    tree = parser.programa()

    listener = MyFinalGrammar()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
