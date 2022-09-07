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
    tabela_variavel = [{"ID": "var1", "TIPO": "int", "ESCOPO": "0"}]
    tabela_funcao = []
    tipo_expressao = ""

    def get_simbolo_variavel(self, id):
        for t in self.tabela_variavel:
            if t["ID"] == id:
                return t

    def verifica_simbolo_variavel(self, id, escopo):

        for t in self.tabela_variavel:
            if t["ID"] == id and t["ESCOPO"] == escopo:
                return True

        for t in self.tabela_funcao:
            if t["ID"] == id:
                return True

        return False

    def insere_variavel_na_tabela(self, tipo, id, escopo):
        self.tabela_variavel.append({"ID":id, "TIPO":tipo, "ESCOPO":escopo})

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

        if self.verifica_id_funcao(id):
            return True

        for b in self.tabela_variavel:
            if b["ID"] == id and b["ESCOPO"] == "0": #duvida!! o id da funçao n pode ser igual ao id de variaveis globai ou locais ou os dois.
                return True

        return False

    def get_parametro_funcao_na_pilha(self):  #retorna os parametros da definiçao da ultima funçao adicionada na piha
        tam = len(self.tabela_funcao)
        if tam > 0:
             return self.tabela_funcao[tam - 1]["PARAMETROS"]

    def verifica_se_variavel_foi_declarada(self, id, escopo):

        for i in self.tabela_variavel:
            if i["id"] == id and i["ESCOPO"] == escopo:
                pass

    def verifica_se_global(self, id):

        for i in self.tabela_variavel:
            if i["id"] == id and i["ESCOPO"] == "0":
                return True

        return False;


    def retorna_tipo_da_variavel(self, id, escopo):
        for i in self.tabela_variavel:
            if i["ID"] == id and i["ESCOPO"] == escopo:
                return i["TIPO"]



    def retorna_escopos_da_variavel(self,id):
        escopos = []

        for i in self.tabela_variavel:
            if i["ID"] == id:
                escopos.append(i["ESCOPO"])

        return escopos

    #---------------------------------------------------------------------------------

    def exitSm_dec_var(self, ctx:finalgrammarParser.Sm_dec_varContext):

        tipo = ctx.TIPO().getText()

        if tipo == "int" or "bool" or "real" or "String":
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise Exception("O Identificador " + i.getText() + " ja foi declarado")

            for i in ctx.ID():
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo))

    def enterAtt_dec_var(self, ctx:finalgrammarParser.Att_dec_varContext):
        tipo = ctx.TIPO().getText()

        n_var = len(ctx.ID())
        n_int = len(ctx.INT())
        n_string = len(ctx.STRING())
        n_real = len(ctx.REAL())
        n_bool = len(ctx.BOOL())
        #trocar o segmento abaixo por um melhor
        if tipo == "int" and n_int == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo))
        elif tipo == "real" and n_real == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo))
        elif tipo == "String" and n_string == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo))
        elif tipo == "bool" and n_bool == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo))
        else:
            raise Exception("Os valores devem ser do mesmo tipo.")


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

    def enterListParam(self, ctx:finalgrammarParser.ListParamContext): #salva os parametros da funçao na ts
        a = []

        lista_tipos = ctx.TIPO()
        lista_ids = ctx.ID()

        for i in range(len(lista_tipos)):
            d = {"ID": lista_ids[i].getText(), "TIPO": lista_tipos[i].getText()}
            a.append(d)

        self.insere_parametros_da_funcao(a)

    def enterCall_func(self, ctx:finalgrammarParser.Call_funcContext): #verifica se o id da chamada da funçao existe
        id_func = ctx.ID().getText()
        if not self.verifica_id_funcao(id_func):
            raise Exception(id_func + " nao existe.")

    def enterInput_stm(self, ctx:finalgrammarParser.Input_stmContext):
        id_var = ctx.ID().getText()
        if not self.verifica_simbolo_variavel(id_var, str(self.escopo)) and not self.verifica_se_global(id_var):
            raise Exception("A variavel " + id_var + " nao foi declarada")

    def enterList_sv(self, ctx: finalgrammarParser.List_svContext):
        if ctx.ID():
            id_list = ctx.ID().getText()
            if not self.verifica_simbolo_variavel(id_list, str(self.escopo)) and not self.verifica_se_global(id_list):
                raise Exception("A variavel " + id_list + "nao existe")

    def enterReturn_stm(self, ctx:finalgrammarParser.Return_stmContext):
        pass


    def exitListParam(self, ctx:finalgrammarParser.ListParamContext):
       pass

    def enterList_callf_param(self, ctx:finalgrammarParser.List_callf_paramContext):
        pass










