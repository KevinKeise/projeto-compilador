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
    tipo_call_func = ""
    id_call_func = ""
    aux_count = 0
    aux_count2 = 0
    is_dep = False

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

        for t in self.tabela_funcao:
            if t["ESCOPO"] == escopo:
                p = t["PARAMETROS"]
                for a in p:
                    if a["ID"] == id:
                        return True

        return False

    def verifica_simbolo_somente_variavel(self, id, escopo):

        for t in self.tabela_variavel:
            if t["ID"] == id and t["ESCOPO"] == escopo:
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

    def retorna_parametros_da_funcao(self, id):

        for t in self.tabela_funcao:
            if t["ID"] == id:
                return t["PARAMETROS"]

        return False

    def verifica_id_funcao(self, id):

        for t in self.tabela_funcao:
            if t["ID"] == id:
                return True

        return False

    def verifica_tipo_funcao(self, id, tipo):

        for t in self.tabela_funcao:
            if t["ID"] == id and t["TIPO"] == tipo:
                return True

        return False

    def verifica_se_funcao_pode_ser_declarada(self, id):

        if self.verifica_id_funcao(id):
            return True

        for b in self.tabela_variavel:
            if b["ID"] == id and b["ESCOPO"] == "0": #duvida!! o id da funçao n pode ser igual ao id de variaveis globai ou locais ou os dois.
                return True

        return False

    def retorna_ultima_funcao_adicionada(self):  #retorna os parametros da definiçao da ultima funçao adicionada na piha
        tam = len(self.tabela_funcao)
        if tam > 0:
             return self.tabela_funcao[tam - 1]

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

        for i in self.tabela_funcao:
            if i["ESCOPO"] == escopo:
                p = i["PARAMETROS"]
                for t in p:
                    if t["ID"] == id:
                        return i["TIPO"]

        return ""



    def retorna_escopos_da_variavel(self,id):
        escopos = []

        for i in self.tabela_variavel:
            if i["ID"] == id:
                escopos.append(i["ESCOPO"])

        return escopos

    def aux_verifica(self, mem, tipo):
        pass

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
            raise Exception("Uma funçao nao pode ter o mesmo no id de outra funcao ou variavel global.")
        else:
            self.insere_funcao_na_tabela(id_func, tipo_func, str(self.escopo))

    def exitFunction(self, ctx:finalgrammarParser.FunctionContext):
        pass

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
        print("ndsdsdsd")
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

        l = self.retorna_ultima_funcao_adicionada();
        if l["TIPO"] == "void":
            raise Exception("A funcao " + l["ID"] + " é do tipo void e nao pode ter retorno.")
        elif l["TIPO"] == "int":
            if ctx.ID():
                id = ctx.ID().getText()
                if not self.verifica_simbolo_somente_variavel(id, str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
                    raise Exception("Variavel " + id + " nao declarada")
                local = self.retorna_tipo_da_variavel(id, str(self.escopo))
                global_var = self.retorna_tipo_da_variavel(id, "0")
                if local != "int" and global_var != "int":
                    raise Exception("Erro: o retorno da funcao" + l["ID"] + "deve ser inteiro")
            elif ctx.expression():
                self.tipo_expressao = "int"
            elif ctx.call_func():
                self.tipo_call_func = "int"

        elif l["TIPO"] == "bool":
            if ctx.ID():
                id = ctx.ID().getText()
                if not self.verifica_simbolo_somente_variavel(id, str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
                    raise Exception("Variavel " + id + " nao declarada")
                local = self.retorna_tipo_da_variavel(id, str(self.escopo))
                global_var = self.retorna_tipo_da_variavel(id, "0")
                if local != "bool" and global_var != "bool":
                    raise Exception("Erro: o retorno da funcao deve ser booleano")
            elif ctx.call_func():
                self.tipo_call_func = "bool"
            elif ctx.BOOL():
                pass
            elif ctx.teste_comp():
                pass

        elif l["TIPO"] == "real":
            if ctx.ID():
                id = ctx.ID().getText()
                if not self.verifica_simbolo_somente_variavel(id, str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
                    raise Exception("Variavel " + id + " nao declarada")
                local = self.retorna_tipo_da_variavel(id, str(self.escopo))
                global_var = self.retorna_tipo_da_variavel(id, "0")
                if local != "real" and global_var != "real":
                    raise Exception("Erro: o retorno da funcao deve ser real")
            elif ctx.expression():
                self.tipo_expressao = "real"
            elif ctx.call_func():
                self.tipo_call_func = "real"
            else:
                raise Exception("Erro: o retorno da funcao deve ser real")

        elif l["TIPO"] == "String":
            if ctx.ID():
                id = ctx.ID().getText()
                if not self.verifica_simbolo_somente_variavel(id, str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
                    raise Exception("Variavel " + id + " nao declarada")
                local = self.retorna_tipo_da_variavel(id, str(self.escopo))
                global_var = self.retorna_tipo_da_variavel(id, "0")
                if local != "String" and global_var != "String":
                    raise Exception("Erro: o retorno da funcao deve ser String")
            elif ctx.call_func():
                self.tipo_call_func = "String"
            elif ctx.STRING():
                pass
            else:
                raise Exception("O tipo de retorno da funçao deve ser String")


    def enterExpression(self, ctx:finalgrammarParser.ExpressionContext):
        if self.tipo_expressao != "":
            if ctx.expr_id():
                pass
            elif ctx.expr_int() and self.tipo_expressao != "int":
                raise Exception("Era esperada uma expressao do tipo " + self.tipo_expressao)
            elif ctx.expr_real() and self.tipo_expressao != "real":
                raise Exception("Era esperada uma expressao do tipo " + self.tipo_expressao)


    def exitExpression(self, ctx:finalgrammarParser.ExpressionContext):
        self.tipo_expressao = ""

    def enterIntIdAri(self, ctx:finalgrammarParser.IntIdAriContext):

        id = ctx.ID().getText()

        type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id, "0")

        if type_id_local != '':
            if type_id_local == 'int':
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo int")
        elif type_id_global != '':
            if type_id_global == 'int':
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo int")
        else:
            raise Exception("A variável " + id + " não existe")

    def enterRealIdAri(self, ctx:finalgrammarParser.RealIdAriContext):

        id = ctx.ID().getText()

        type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id, "0")

        if type_id_local != '':
            if type_id_local == 'real':
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo real")
        elif type_id_global != '':
            if type_id_global == 'real':
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo real")
        else:
            raise Exception("A variável " + id + " não existe")

    def enterCall_func(self, ctx:finalgrammarParser.Call_funcContext):
        id_func = ctx.ID().getText()


        if self.verifica_id_funcao(id_func):
            self.id_call_func = id_func
            num_param = len(ctx.list_callf_param())
            param = len(self.retorna_parametros_da_funcao(id_func))
            if num_param == 0 and param != 0:
                raise Exception("O número de parametros passados a chamada da funçao " + id_func + " nao é compativel com a definiçao.")
        else:
            raise Exception("A funçao " + id_func + " nao existe.")

        if self.tipo_call_func != "":
            if self.verifica_tipo_funcao(id_func,self.tipo_call_func):
                pass
            else:
                raise Exception("A funçao " + ctx.ID().getText() + " nao pode ser chamada nesse escopo.")

    def exitCall_func(self, ctx: finalgrammarParser.Call_funcContext):
        self.tipo_call_func = ""
        self.id_call_func = ""
        self.num_param = 0
        if self.is_dep == False:
            self.aux_count = 0
        self.is_dep = False
        self.aux_count2 = 0

    def exitListParam(self, ctx:finalgrammarParser.ListParamContext):
       pass

    def enterList_callf_param(self, ctx:finalgrammarParser.List_callf_paramContext):

        param = self.retorna_parametros_da_funcao(self.id_call_func)
        num_fun = len(param)
        num_param = len(ctx.list_callf())

        if param != False:
            print(num_param)
            if num_fun != num_param:
                raise Exception("O número de parametros passados a chamada da funçao " + self.id_call_func + " nao é compativel com a definiçao.")


    def enterList_callf(self, ctx:finalgrammarParser.List_callfContext):

        param = self.retorna_parametros_da_funcao(self.id_call_func)  # Busca os parametros passados na definiçao da funçao

        if self.is_dep == False:
            tipo = param[self.aux_count]["TIPO"]
        else:
            tipo = param[self.aux_count2]["TIPO"]

        if ctx.ID():

            id = ctx.ID().getText()

            tipo_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
            tipo_global = self.retorna_tipo_da_variavel(id, "0")

            if tipo_local != "":
                if tipo_local != tipo:
                    raise Exception("O tipo da ")
            elif tipo_global != "":
                if tipo_global != tipo:
                    raise Exception("asdasdasda")
            else:
                raise Exception("Erro")

            if self.is_dep == False:
                self.aux_count = self.aux_count + 1
            else:
                self.aux_count2 = self.aux_count2 + 1

        elif ctx.BOOL():
            pass
        elif ctx.STRING():
            pass
        elif ctx.expression():
            self.tipo_expressao = tipo
            self.aux_count = self.aux_count + 1
        elif ctx.call_func():
            if self.is_dep == True:
                raise Exception("Erroukkkk")
            self.tipo_call_func = tipo
            self.is_dep = True
















