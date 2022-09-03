# Generated from C:/Users/kevin/OneDrive/�rea de Trabalho/trabalho-final\finalgrammar.g4 by ANTLR 4.10.1
from antlr4 import *
from gen.finalgrammarListener import finalgrammarListener
if __name__ is not None and "." in __name__:
    from .finalgrammarParser import finalgrammarParser
else:
    from finalgrammarParser import finalgrammarParser


# This class defines a complete listener for a parse tree produced by finalgrammarParser.
class MyFinalGrammar(finalgrammarListener):

    escopo = 0
    tabela_variavel_global = [{"ID":"var1","TIPO":"int","ESCOPO":"0"}]
    tabela_funcao = []

    def get_simbolo_variavel(self, id):
        for t in self.tabela_variavel_global:
            if t["ID"] == id:
                return t

    def verifica_simbolo_variavel(self, tipo, id, escopo):

        for t in self.tabela_variavel_global:
            if t["ID"] == id and t["ESCOPO"] == escopo and t["TIPO"] == tipo:
                return True

        return False

    def insere_na_tabela(self, tipo, id, escopo):
        self.tabela_variavel_global.append({"ID":id,"TIPO":tipo,"ESCOPO":escopo})

    def insere_funcao_na_tabela(self, id, tipo, escopo):
        self.tabela_funcao.append({"ID": id, "TIPO": tipo, "ESCOPO":escopo, "PARAMETROS":[]})

    def insere_parametros_da_funcao(self, parametros):
        tam = len(self.tabela_funcao)
        if tam > 0:
            self.tabela_funcao[tam - 1]["PARAMETROS"] = parametros

    def verifica_id_funcao(self, id):
        for t in self.tabela_funcao:
            if t["ID"] == id:
                return True
        return False

    def verifica_se_funcao_pode_ser_declarada(self, id):

        for t in self.tabela_funcao:
            if t["ID"] == id:
                return True

        for b in self.tabela_variavel_global:
            if b["ID"] == id and b["ESCOPO"] == "0":
                return True

        return False

    #---------------------------------------------------------------------------------

    def exitSm_dec_var(self, ctx:finalgrammarParser.Sm_dec_varContext):

        tipo = ctx.TIPO().getText()

        if tipo == "int" or "bool" or "real" or "String":
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(tipo, i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."

            for i in ctx.ID():
                self.insere_na_tabela(tipo, i.getText(), str(self.escopo))

    def enterAtt_dec_var(self, ctx:finalgrammarParser.Att_dec_varContext):
        tipo = ctx.TIPO().getText()

        n_var = len(ctx.ID())
        n_int = len(ctx.INT())
        n_string = len(ctx.STRING())
        n_real = len(ctx.REAL())
        n_bool = len(ctx.BOOL())

        if tipo == "int" and n_int == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(tipo, i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_na_tabela(tipo, i.getText(), str(self.escopo))
        elif tipo == "real" and n_real == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(tipo, i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_na_tabela(tipo, i.getText(), str(self.escopo))
        elif tipo == "String" and n_string == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(tipo, i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_na_tabela(tipo, i.getText(), str(self.escopo))
        elif tipo == "bool" and n_bool == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(tipo, i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_na_tabela(tipo, i.getText(), str(self.escopo))
        else:
            raise "Os valores deve ser do mesmo tipo."


    def exitPrint_stm(self, ctx:finalgrammarParser.Print_stmContext):
        pass

    def enterFunction(self, ctx:finalgrammarParser.FunctionContext):
        self.escopo = self.escopo + 1
        tipo_func = ctx.TIPO().getText()
        id_func = ctx.ID().getText()

        if self.verifica_se_funcao_pode_ser_declarada(id_func):
            raise "Uma funçao nao pode ter o mesmo no id de outra funcao ou variavel global."
        else:
            self.insere_funcao_na_tabela(id_func, tipo_func, str(self.escopo))

    def exitFunction(self, ctx:finalgrammarParser.FunctionContext):
        print(self.tabela_funcao)

    def enterMain_function(self, ctx:finalgrammarParser.Main_functionContext):
        self.escopo = self.escopo + 1

    def enterListParam(self, ctx:finalgrammarParser.ListParamContext):
        a = []
        lista_tipos = ctx.TIPO()
        lista_ids = ctx.ID()
        for i in range(len(lista_tipos)):
            d = {"ID": lista_ids[i].getText(), "TIPO": lista_tipos[i].getText()}
            a.append(d)

        self.insere_parametros_da_funcao(a)

    def enterCall_func(self, ctx:finalgrammarParser.Call_funcContext):
        id_func = ctx.ID().getText()
        if not self.verifica_id_funcao(id_func):
            raise Exception(id_func + " nao existe")


    def exitListParam(self, ctx:finalgrammarParser.ListParamContext):
       pass










