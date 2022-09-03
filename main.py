from antlr4 import *
from gen.MyFinalGrammar import MyFinalGrammar
from gen.finalgrammarLexer import finalgrammarLexer
from gen.finalgrammarParser import finalgrammarParser

if __name__ == '__main__':
    exp = 'real var111 = 2.4,var113=56.34; def var11(real abc, int qwe) void {int v = 2;print(v);}def main(){int ai = 2;print("ao","asd");var1167();m = 34+var;}'
    data = InputStream(exp)

    lexer = finalgrammarLexer(data)
    tokens = CommonTokenStream(lexer)

    parser = finalgrammarParser(tokens)
    tree = parser.programa()

    listener = MyFinalGrammar()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
