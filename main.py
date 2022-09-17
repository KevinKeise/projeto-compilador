from antlr4 import *
from gen.MyFinalGrammar import MyFinalGrammar
from gen.finalgrammarLexer import finalgrammarLexer
from gen.finalgrammarParser import finalgrammarParser

if __name__ == '__main__':
    exp = 'real var111 = 2.4,var113=56.8;real va;def v(bool var,int b) int {int jk;int cb;return jk+cb;}def vic(bool a, int asd) bool {} def main(){int l;bool b;int m;print("asd");v(vic(b,3),l);m = 4;}'
    data = InputStream(exp)

    lexer = finalgrammarLexer(data)
    tokens = CommonTokenStream(lexer)

    parser = finalgrammarParser(tokens)
    tree = parser.programa()

    listener = MyFinalGrammar()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
