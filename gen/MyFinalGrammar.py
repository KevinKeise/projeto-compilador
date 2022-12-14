# Generated from C:/Users/kevin/OneDrive/�rea de Trabalho/trabalho-final\finalgrammar.g4 by ANTLR 4.10.1
from antlr4 import *
from gen.finalgrammarListener import finalgrammarListener
if __name__ is not None and "." in __name__:
    from .finalgrammarParser import finalgrammarParser
else:
    from finalgrammarParser import finalgrammarParser

from .func import le_arquivo, escreve_arquivo

# This class defines a complete listener for a parse tree produced by finalgrammarParser.
class MyFinalGrammar(finalgrammarListener):

    data = le_arquivo("code.py")
    data_lines = data.splitlines()
    text_file_out = ""
    escopo = 0
    tabela_variavel = []
    tabela_funcao = []
    tipo_expressao = ""
    tipo_call_func = ""
    id_call_func = ""
    aux_count = 0
    aux_count2 = 0
    is_dep = False
    aux_func = ""
    endereco = 0
    p_j_c = ""
    cont_att = ""
    end_var = ""

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

    def insere_variavel_na_tabela(self, tipo, id, escopo, end, valor):
        self.tabela_variavel.append({"ID":id, "TIPO":tipo, "ESCOPO":escopo, "ENDERECO": end, "VALOR":valor})

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
            if i["ID"] == id and i["ESCOPO"] == escopo:
                pass

    def verifica_se_global(self, id):

        for i in self.tabela_variavel:
            if i["ID"] == id and i["ESCOPO"] == "0":
                return True

        return False;

    def retorna_tipo_funcao(self, id):

        for t in self.tabela_funcao:
            if t["ID"] == id:
                return t["TIPO"]

        return ""


    def retorna_tipo_da_variavel(self, id, escopo):

        for i in self.tabela_variavel:
            if i["ID"] == id and i["ESCOPO"] == escopo:
                return i["TIPO"]

        for i in self.tabela_funcao:
            if i["ESCOPO"] == escopo:
                p = i["PARAMETROS"]
                for t in p:
                    if t["ID"] == id:
                        return t["TIPO"]

        return ""



    def retorna_escopos_da_variavel(self,id):
        escopos = []

        for i in self.tabela_variavel:
            if i["ID"] == id:
                escopos.append(i["ESCOPO"])

        return escopos

    def aux_verifica(self, mem, tipo):
        pass

    def conta_qtd_variaveis(self, escopo):

        qtd = 0

        for i in self.tabela_variavel:
            if i["ESCOPO"] == escopo:
                qtd += 1

        return qtd

    def retorna_endereco_var(self, id, escopo):
        for i in self.tabela_variavel:
            if i["ID"] == id and i["ESCOPO"] == escopo:
                return i["ENDERECO"]
        return None

    #---------------------------------------------------------------------------------

    def enterPrograma(self, ctx:finalgrammarParser.ProgramaContext):
        self.text_file_out += ".class public finalgrammar\n.super java/lang/Object\n\n"


    def exitSm_dec_var(self, ctx:finalgrammarParser.Sm_dec_varContext):

        tipo = ctx.TIPO().getText()

        if tipo == "int" or "bool" or "real" or "String":
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise Exception("O Identificador " + i.getText() + " ja foi declarado")

            for i in ctx.ID():
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo), self.endereco, None)
                self.endereco += 1



    def enterAtt_dec_var(self, ctx:finalgrammarParser.Att_dec_varContext):
        tipo = ctx.TIPO().getText()

        aux = 0

        n_var = len(ctx.ID())
        n_int = len(ctx.INT())
        n_string = len(ctx.STRING())
        n_real = len(ctx.REAL())
        n_bool = len(ctx.BOOL())

        #trocar o segmento abaixo por um melhor
        if tipo == "int" and n_int == n_var:
            for i in ctx.ID():
                print(ctx.INT()[aux].getText())
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo), self.endereco, ctx.INT()[aux].getText())
                aux += 1
                self.endereco += 1

        elif tipo == "real" and n_real == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo), self.endereco,ctx.REAL()[aux].getText())
                aux += 1
                self.endereco += 1
        elif tipo == "String" and n_string == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo), self.endereco, ctx.STRING()[aux].getText())
                aux += 1
                self.endereco += 1
        elif tipo == "bool" and n_bool == n_var:
            for i in ctx.ID():
                if self.verifica_simbolo_variavel(i.getText(), str(self.escopo)):
                    raise "Variável () já declarada."
                self.insere_variavel_na_tabela(tipo, i.getText(), str(self.escopo), self.endereco, ctx.BOOL()[aux].getText())
                aux += 1
                self.endereco += 1
        else:
            raise Exception("Os valores devem ser do mesmo tipo.")


    def exitAtt_dec_var(self, ctx: finalgrammarParser.Att_dec_varContext):
        if ctx.INT():
            for i in ctx.INT():
                pass
        elif ctx.REAL():
            pass
        elif ctx.BOOL():
            pass
        elif ctx.STRING():
            pass

    def exitDecVar(self, ctx:finalgrammarParser.DecVarContext):
        pass

    def exitInitial_vars(self, ctx:finalgrammarParser.Initial_varsContext):
        qtd = self.conta_qtd_variaveis(str(self.escopo))
        if qtd > 0:
            self.text_file_out += f"    .limit locals {qtd}\n"

        for i in self.tabela_variavel:
            if i["VALOR"] != None and i["ESCOPO"] == str(self.escopo):
                val = i["VALOR"]
                end = i["ENDERECO"]
                if i["TIPO"] == "int":
                    self.text_file_out += f"\tldc {val}\n"
                    self.text_file_out += f"\tistore {end}\n"
                elif i["TIPO"] == "real":
                    self.text_file_out += f"\tldc {val}\n"
                    self.text_file_out += f"\tistore {end}\n"
                elif i["TIPO"] == "bool":
                    if val == "True":
                        self.text_file_out += f"\tldc 1\n"
                        self.text_file_out += f"\tistore {end}\n"
                    else:
                        self.text_file_out += f"\tldc 0\n"
                        self.text_file_out += f"\tistore {end}\n"
                elif i["TIPO"] == "String":
                    pass



    def enterAtt_e(self, ctx:finalgrammarParser.Att_eContext):
        id = ctx.ID().getText()

        type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id, "0")

        if type_id_local == "" and type_id_global == "":
            raise Exception("A Variável " + id + "nao foi declarada.")

        if ctx.BOOL():
            if type_id_local == "bool" or type_id_global == "bool":
                text = ctx.BOOL().getText()
                if type_id_local == "bool":
                    end = self.retorna_endereco_var(id, str(self.escopo))
                    if text == "True":
                        self.text_file_out += "\tldc 1\n"
                    else:
                        self.text_file_out += "\tldc 0\n"
                    self.text_file_out += f"\tistore {end}\n"
                else:
                    end = self.retorna_endereco_var(id, "0")
                    if text == "True":
                        self.text_file_out += "\tldc 1\n"
                    else:
                        self.text_file_out += "\tldc 0\n"
                    self.text_file_out += f"\tistore {end}\n"
            else:
                raise Exception("A expressao " + ctx.getText() + " deve ser do tipo bool.")
        elif ctx.STRING():
            if type_id_local == "String" or type_id_global == "String":
                pass
            else:
                raise Exception("A expressao " + ctx.getText() + " deve ser do tipo String.")
        elif ctx.expression():
            if type_id_local != "":
                self.tipo_expressao = type_id_local
                if type_id_local == "int":
                    self.cont_att = "int"
                else:
                    self.cont_att = "real"
            else:
                self.tipo_expressao = type_id_global
                if type_id_global == "int":
                    self.cont_att = "int"
                else:
                    self.cont_att = "real"

    def exitAtt_e(self, ctx: finalgrammarParser.Att_eContext):
        id = ctx.ID().getText()
        end_local = self.retorna_endereco_var(id, str(self.escopo))
        end_global = self.retorna_endereco_var(id, "0")
        if end_local != None:
            if self.cont_att == "int":
                self.text_file_out += f"\tistore {end_local}\n"
            elif self.cont_att == "real":
                self.text_file_out += f"\tfstore {end_local}\n"
        else:
            if self.cont_att == "int":
                self.text_file_out += f"\tistore {end_global}\n"
            elif self.cont_att == "real":
                self.text_file_out += f"\tfstore {end_global}\n"

        self.cont_att = ""

    def enterAtt_s(self, ctx:finalgrammarParser.Att_sContext):
        id_1 = ctx.ID()[0].getText()

        type_id_local = self.retorna_tipo_da_variavel(id_1, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id_1, "0")

        if type_id_local == "" and type_id_global == "":
            raise Exception("A Variável " + id_1 + "nao foi declarada.")

        if len(ctx.ID()) > 1:
            id_2 = ctx.ID()[1].getText()

            type_id_local_2 = self.retorna_tipo_da_variavel(id_2, str(self.escopo))
            type_id_global_2 = self.retorna_tipo_da_variavel(id_2, "0")

            if type_id_local != "":
                ty = type_id_local
            elif type_id_global != "":
                ty = type_id_global

            if type_id_local_2 == "" and type_id_global_2 == "":
                raise Exception("A Variável " + id_2 + "nao foi declarada.")

            if type_id_local_2 != '':
                if type_id_local_2 == ty:
                    pass
                else:
                    raise Exception("A variável " + id_2 + " deve ser do tipo " + ty)
            elif type_id_global_2 != '':
                if type_id_global_2 == ty:
                    pass
                else:
                    raise Exception("A variável " + id_2 + " deve ser do tipo " + ty)
            else:
                raise Exception("A variável " + id_2 + " não existe")

        elif ctx.REAL():
            if type_id_local == "real" or type_id_global == "real":
                pass
            else:
                raise Exception("A expressao " + ctx.getText() + " deve ser do tipo real.")
        elif ctx.INT():
            if type_id_local == "int" or type_id_global == "int":
                pass
            else:
                raise Exception("A expressao " + ctx.getText() + " deve ser do tipo int.")
        else:
            raise Exception("Erro de tipo.")


    def enterAtt_m(self, ctx:finalgrammarParser.Att_mContext):
        id_1 = ctx.ID()[0].getText()

        type_id_local = self.retorna_tipo_da_variavel(id_1, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id_1, "0")

        if type_id_local == "" and type_id_global == "":
            raise Exception("A Variável " + id_1 + "nao foi declarada.")

        if len(ctx.ID()) > 1:
            id_2 = ctx.ID()[1].getText()

            type_id_local_2 = self.retorna_tipo_da_variavel(id_2, str(self.escopo))
            type_id_global_2 = self.retorna_tipo_da_variavel(id_2, "0")

            if type_id_local != "":
                ty = type_id_local
            elif type_id_global != "":
                ty = type_id_global

            if type_id_local_2 == "" and type_id_global_2 == "":
                raise Exception("A Variável " + id_2 + "nao foi declarada.")

            if type_id_local_2 != '':
                if type_id_local_2 == ty:
                    pass
                else:
                    raise Exception("A variável " + id_2 + " deve ser do tipo " + ty)
            elif type_id_global_2 != '':
                if type_id_global_2 == ty:
                    pass
                else:
                    raise Exception("A variável " + id_2 + " deve ser do tipo " + ty)
            else:
                raise Exception("A variável " + id_2 + " não existe")

        elif ctx.REAL():
            if type_id_local == "real" or type_id_global == "real":
                pass
            else:
                raise Exception("A expressao " + ctx.getText() + " deve ser do tipo real.")
        elif ctx.INT():
            if type_id_local == "int" or type_id_global == "int":
                pass
            else:
                raise Exception("A expressao " + ctx.getText() + " deve ser do tipo int.")
        else:
            raise Exception("Erro de tipo.")

    def exitPrint_stm(self, ctx:finalgrammarParser.Print_stmContext):
        pass

    def enterPrint_stm(self, ctx:finalgrammarParser.Print_stmContext):
        pass


    def enterFunction(self, ctx:finalgrammarParser.FunctionContext):
        self.endereco = 0
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
        self.text_file_out += ".method public static main([Ljava/lang/String;)V \n"
        self.escopo = self.escopo + 1
        self.insere_funcao_na_tabela("main", "void", str(self.escopo))
        self.endereco = 0

    def exitMain_function(self, ctx:finalgrammarParser.Main_functionContext):
        self.text_file_out += ".end method"
        escreve_arquivo(self.text_file_out)


    def enterListParam(self, ctx:finalgrammarParser.ListParamContext): #salva os parametros da funçao na ts
        a = []

        lista_tipos = ctx.TIPO()
        lista_ids = ctx.ID()
        for i in range(len(lista_tipos)):
            d = {"ID": lista_ids[i].getText(), "TIPO": lista_tipos[i].getText()}
            a.append(d)

        self.insere_parametros_da_funcao(a)

    def enterInput_stm(self, ctx:finalgrammarParser.Input_stmContext):
        id_var = ctx.ID().getText()
        if not self.verifica_simbolo_variavel(id_var, str(self.escopo)) and not self.verifica_se_global(id_var):
            raise Exception("A variavel " + id_var + " nao foi declarada")

    def enterPrintString(self, ctx:finalgrammarParser.PrintStringContext):
        self.text_file_out += "\tgetstatic java/lang/System/out Ljava/io/PrintStream;\n"
        self.text_file_out += "\tldc " + f"{ctx.STRING().getText()}"  + "\n"
        self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(Ljava/lang/String;)V\n"

    def enterPrintId(self, ctx:finalgrammarParser.PrintIdContext):
        id_list = ctx.ID().getText()

        if not self.verifica_simbolo_variavel(id_list, str(self.escopo)) and not self.verifica_se_global(id_list):
            raise Exception("A variavel " + id_list + "nao existe")

        local = self.retorna_endereco_var(id_list,str(self.escopo))
        global_var = self.retorna_endereco_var(id_list, "0")

        if local != None:
            tipo = self.retorna_tipo_da_variavel(id_list, str(self.escopo))
            self.text_file_out += "\tgetstatic java/lang/System/out Ljava/io/PrintStream;\n"
            if tipo == "int":
                self.text_file_out += f"\tiload {local}\n"
                self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(I)V\n"
            elif tipo == "real":
                self.text_file_out += f"\tfload {local}\n"
                self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(F)V\n"
            elif tipo == "bool":
                self.text_file_out += f"\tiload {local}\n"
                self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(I)V\n"
            elif tipo == "String":
                self.text_file_out += f"Como faz pra carregar uma string de uma variavel?"
                self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(Ljava/lang/String;)V\n"

        elif global_var != "":
            tipo = self.retorna_tipo_da_variavel(id_list, "0")

            self.text_file_out += "\tgetstatic java/lang/System/out Ljava/io/PrintStream;\n"
            if tipo == "int":
                self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(I)V\n"
            elif tipo == "real":
                self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(F)V\n"

    def enterPrintExpression(self, ctx:finalgrammarParser.PrintExpressionContext):
        self.text_file_out += "\tgetstatic java/lang/System/out Ljava/io/PrintStream;\n"

    def exitPrintExpression(self, ctx:finalgrammarParser.PrintExpressionContext):
        if self.p_j_c == "int":
            self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(I)V\n"
            self.p_j_c = ""
        elif self.p_j_c == "real":
            self.text_file_out += "\tinvokevirtual java/io/PrintStream/println(F)V\n"
            self.p_j_c = ""

    def exitReturn_stm(self, ctx: finalgrammarParser.Return_stmContext):
        l = self.retorna_ultima_funcao_adicionada();
        if l["TIPO"] == "void":
            self.text_file_out += "\treturn\n"
        elif l["TIPO"] == "int":
            if ctx.ID():
                id = ctx.ID().getText()
                if not self.verifica_simbolo_somente_variavel(id,str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
                    raise Exception("Variavel " + id + " nao declarada")
                local = self.retorna_tipo_da_variavel(id, str(self.escopo))
                global_var = self.retorna_tipo_da_variavel(id, "0")
                if local != "int" and global_var != "int":
                    raise Exception("Erro: o retorno da funcao" + l["ID"] + "deve ser inteiro")
                if local == "int":
                    end = self.retorna_endereco_var(id, str(self.escopo))
                    self.text_file_out += f"\tiload {end}\n"
                    self.text_file_out += f"\tireturn\n"
                elif global_var == "int":
                    end = self.retorna_endereco_var(id, "0")
                    self.text_file_out += f"\tiload {end}\n"
                    self.text_file_out += f"\tireturn\n"
            elif ctx.expression():
                self.tipo_expressao = "int"
                self.text_file_out += f"\tireturn\n"
            elif ctx.call_func():
                self.tipo_call_func = "int"
                self.text_file_out += f"\tireturn\n"

        elif l["TIPO"] == "bool":
            if ctx.ID():
                id = ctx.ID().getText()
                if not self.verifica_simbolo_somente_variavel(id,str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
                    raise Exception("Variavel " + id + " nao declarada")
                local = self.retorna_tipo_da_variavel(id, str(self.escopo))
                global_var = self.retorna_tipo_da_variavel(id, "0")
                if local != "bool" and global_var != "bool":
                    raise Exception("Erro: o retorno da funcao deve ser booleano")
                if local == "int":
                    end = self.retorna_endereco_var(id, str(self.escopo))
                    self.text_file_out += f"\tiload {end}\n"
                    self.text_file_out += f"\tireturn\n"
                elif global_var == "int":
                    end = self.retorna_endereco_var(id, "0")
                    self.text_file_out += f"\tiload {end}\n"
                    self.text_file_out += f"\tireturn\n"
            elif ctx.call_func():
                self.tipo_call_func = "bool"
                self.text_file_out += f"\tireturn\n"
            elif ctx.BOOL():
                res = ctx.BOOL().getText()
                if res == "True":
                    self.text_file_out += f"\tldc 1\n"
                    self.text_file_out += f"\tireturn\n"
            elif ctx.teste_comp():
                pass

        elif l["TIPO"] == "real":
            if ctx.ID():
                id = ctx.ID().getText()
                if not self.verifica_simbolo_somente_variavel(id,str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
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
                if not self.verifica_simbolo_somente_variavel(id,str(self.escopo)) and not self.verifica_simbolo_somente_variavel(id, "0"):
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

        if ctx.expr_int():
            self.p_j_c = "int"
            print(self.p_j_c,"asd")
        elif ctx.expr_real():
            self.p_j_c = "real"

        if self.tipo_expressao != "":
            if ctx.expr_id():
                pass
            elif ctx.expr_int() and self.tipo_expressao != "int":
                raise Exception("Era esperada uma expressao do tipo " + self.tipo_expressao)
            elif ctx.expr_real() and self.tipo_expressao != "real":
                raise Exception("Era esperada uma expressao do tipo " + self.tipo_expressao)



    def exitExpression(self, ctx:finalgrammarParser.ExpressionContext):
        self.tipo_expressao = ""

    def exitIntSoma(self, ctx:finalgrammarParser.IntSomaContext):
        self.text_file_out += "\tiadd\n"

    def exitIntSubtracao(self, ctx:finalgrammarParser.IntSubtracaoContext):
        self.text_file_out += "\tisub\n"

    def exitIntMulti(self, ctx:finalgrammarParser.IntMultiContext):

        self.text_file_out += "\timul\n"

    def exitIntDiv(self, ctx:finalgrammarParser.IntDivContext):

        self.text_file_out += "\tidiv\n"

    def enterIntIdAri(self, ctx:finalgrammarParser.IntIdAriContext):

        id = ctx.ID().getText()

        type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id, "0")

        if type_id_local != '':
            if type_id_local == 'int':
                self.tipo_expressao = "int"
                endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                self.text_file_out += f"\tiload {endereco_var}\n"
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo int")
        elif type_id_global != '':
            if type_id_global == 'int':
                self.tipo_expressao = "int"
                endereco_var = self.retorna_endereco_var(id, "0")
                self.text_file_out += f"\tiload {endereco_var}\n"
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo int")
        else:
            raise Exception("A variável " + id + " não existe")

    def enterIntInteiroAri(self, ctx:finalgrammarParser.IntInteiroAriContext):
        num = ctx.INT().getText()
        self.text_file_out += f"\tldc {str(num)}\n"

    def enterIntCallFuncAri(self, ctx:finalgrammarParser.IntCallFuncAriContext):
        self.tipo_call_func = "int"

    def enterIntMenosUnarioAri(self, ctx:finalgrammarParser.IntMenosUnarioAriContext):
        self.text_file_out += "\tineg\n"

    def enterRealAri(self, ctx:finalgrammarParser.RealAriContext):
        num = ctx.REAL().getText()
        self.text_file_out += f"\tldc {str(num)}\n"

    def exitRealSoma(self, ctx:finalgrammarParser.RealSomaContext):
        self.text_file_out += "\tfadd\n"

    def exitRealSubtracao(self, ctx:finalgrammarParser.RealSubtracaoContext):
        self.text_file_out += "\tfsub\n"

    def exitRealMulti(self, ctx:finalgrammarParser.RealMultiContext):
        self.text_file_out += "\tfmul\n"

    def exitRealDiv(self, ctx:finalgrammarParser.RealDivContext):
        self.text_file_out += "\tfdiv\n"

    def enterRealIdAri(self, ctx:finalgrammarParser.RealIdAriContext):

        id = ctx.ID().getText()

        type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id, "0")

        if type_id_local != '':
            if type_id_local == 'real':
                endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                self.text_file_out += f"\tfload {endereco_var}\n"
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo real")
        elif type_id_global != '':
            if type_id_global == 'real':
                endereco_var = self.retorna_endereco_var(id, "0")
                self.text_file_out += f"\tfload {endereco_var}\n"
                pass
            else:
                raise Exception("A variável " + id + " deve ser do tipo real")
        else:
            raise Exception("A variável " + id + " não existe")



    def enterRealCallFuncAri(self, ctx:finalgrammarParser.RealCallFuncAriContext):
        self.tipo_call_func = "real"


    def exitIdSoma(self, ctx:finalgrammarParser.IdSomaContext):
        if self.tipo_expressao == "int":
            self.text_file_out += "\tiadd\n"
        elif self.tipo_expressao == "real":
            self.text_file_out += "\tfadd\n"
        print(self.tipo_expressao)

    def exitIdSubtracao(self, ctx:finalgrammarParser.IdSubtracaoContext):
        if self.tipo_expressao == "int":
            self.text_file_out += "\tisub\n"
        elif self.tipo_expressao == "real":
            self.text_file_out += "\tfsub\n"
        print(self.tipo_expressao)

    def exitIdMulti(self, ctx:finalgrammarParser.IdMultiContext):
        if self.tipo_expressao == "int":
            self.text_file_out += "\timul\n"
        elif self.tipo_expressao == "real":
            self.text_file_out += "\tfmul\n"
        print(self.tipo_expressao)

    def exitIdDiv(self, ctx:finalgrammarParser.IdDivContext):
        if self.tipo_expressao == "int":
            self.text_file_out += "\tidiv\n"
        elif self.tipo_expressao == "real":
            self.text_file_out += "\tfdiv\n"
        print(self.tipo_expressao)

    def enterIdIdAri(self, ctx:finalgrammarParser.IdIdAriContext):

        if self.tipo_expressao != "":
            id = ctx.ID().getText()

            type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
            type_id_global = self.retorna_tipo_da_variavel(id, "0")

            if type_id_local != '':
                if type_id_local == self.tipo_expressao:
                    if type_id_local == "int":
                        self.p_j_c = "int"
                        endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                        self.text_file_out += f"\tiload {endereco_var}\n"
                    elif type_id_local == "real":
                        self.p_j_c = "real"
                        endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                        self.text_file_out += f"\tfload {endereco_var}\n"
                else:
                    raise Exception("A variável " + id + " deve ser do tipo " + self.tipo_expressao)
            elif type_id_global != '':
                if type_id_global == self.tipo_expressao:
                    if type_id_global == "int":
                        self.p_j_c = "int"
                        endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                        self.text_file_out += f"\tiload {endereco_var}\n"
                    elif type_id_global == "real":
                        self.p_j_c = "real"
                        endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                        self.text_file_out += f"\tfload {endereco_var}\n"
                else:
                    raise Exception("A variável " + id + " deve ser do tipo " + self.tipo_expressao)
            else:
                raise Exception("A variável " + id + " não existe")
        else:
            id = ctx.ID().getText()

            type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
            type_id_global = self.retorna_tipo_da_variavel(id, "0")

            if type_id_local != '':
                self.tipo_expressao = type_id_local
                if type_id_local == "int":
                    endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                    self.text_file_out += f"\tiload {endereco_var}\n"
                elif type_id_local == "real":
                    endereco_var = self.retorna_endereco_var(id, str(self.escopo))
                    self.text_file_out += f"\tfload {endereco_var}\n"
            elif type_id_global != '':
                self.tipo_expressao = type_id_global
                if type_id_local == "int":
                    endereco_var = self.retorna_endereco_var(id, "0")
                    self.text_file_out += f"\tiload {endereco_var}\n"
                elif type_id_local == "real":
                    endereco_var = self.retorna_endereco_var(id, "0")
                    self.text_file_out += f"\tfload {endereco_var}\n"
            else:
                raise Exception("A variável " + id + " não existe")

    def enterIdCallFuncAri(self, ctx:finalgrammarParser.IdCallFuncAriContext):
        if self.tipo_expressao == "int":
            self.tipo_call_func == "int"
        elif self.tipo_expressao == "real":
            self.tipo_expressao = "real"

    def enterIdcompFact(self, ctx:finalgrammarParser.IdcompFactContext):
        id = ctx.ID().getText()

        type_id_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
        type_id_global = self.retorna_tipo_da_variavel(id, "0")

        if type_id_local != '':
            if type_id_local == "int" or type_id_local == "bool":
                end = self.retorna_endereco_var(id, str(self.escopo))
                self.text_file_out += f"iload {end}"
            elif type_id_local == "real":
                end = self.retorna_endereco_var(id, str(self.escopo))
                self.text_file_out += f"fload {end}"

        elif type_id_global != '':
            if type_id_local == "int" or type_id_local == "bool":
                end = self.retorna_endereco_var(id, "0")
                self.text_file_out += f"iload {end}"
            elif type_id_local == "real":
                end = self.retorna_endereco_var(id, "0")
                self.text_file_out += f"fload {end}"
        else:
            raise Exception("A variável " + id + " não existe")

    def enterFor_stm(self, ctx:finalgrammarParser.For_stmContext):
        id_arr = ctx.ID()

        typ_local = self.retorna_tipo_da_variavel(id_arr, str(self.escopo))
        typ_global = self.retorna_tipo_da_variavel(id_arr, "0")

        if typ_local != "":
            if typ_local != "int":
                raise Exception("As variaveis do laço for devem ser do tipo int.")
        elif typ_global != "":
            if typ_local != "int":
                raise Exception("As variaveis do laço for devem ser do tipo int.")
        else:
            Exception("A variavel " + id_arr + " nao existe.")

    def enterFor_stm_types(self, ctx:finalgrammarParser.For_stm_typesContext):
        id_arr = ctx.ID()

        typ_local = self.retorna_tipo_da_variavel(id_arr, str(self.escopo))
        typ_global = self.retorna_tipo_da_variavel(id_arr, "0")

        if typ_local != "":
            if typ_local != "int":
                raise Exception("As variáveis do laço for devem ser do tipo int.")
        elif typ_global != "":
            if typ_local != "int":
                raise Exception("As variáveis do laço for devem ser do tipo int.")
        else:
            Exception("A variavel " + id_arr + " nao existe.")

    def enterCall_func(self, ctx:finalgrammarParser.Call_funcContext):
        id_func = ctx.ID().getText()

        if self.verifica_id_funcao(id_func):
            if self.is_dep == True:
                self.aux_func = id_func
            else:
                self.id_call_func = id_func
            num_param = len(ctx.list_callf_param())
            param = len(self.retorna_parametros_da_funcao(id_func))
            if num_param == 0 and param != 0:
                raise Exception("O número de parametros passados a chamada da funçao " + id_func + " nao é compativel com a definiçao.")
        else:
            raise Exception("A funçao " + id_func + " nao existe.")

        if self.tipo_call_func != "":
            if self.verifica_tipo_funcao(id_func , self.tipo_call_func):
                if self.tipo_call_func == "int":
                    self.text_file_out += f"invokestatic finnalgrammar.{str(id_func)}()I"
                elif self.tipo_call_func == "real":
                    self.text_file_out += f"invokestatic finnalgrammar.{str(id_func)}()F"
                elif self.tipo_call_func == "String":
                    self.text_file_out += f"invokestatic finnalgrammar.{str(id_func)}() retorna String"
                elif self.tipo_call_func == "bool":
                    self.text_file_out += f"invokestatic finnalgrammar.{str(id_func)}() retorna bool"
            else:
                raise Exception("O retorno da funçao " + ctx.ID().getText() + " deve ser " + self.tipo_call_func +".")
        else:
            type_func = self.retorna_tipo_funcao(id_func)
            self.tipo_expressao = type_func

    def exitCall_func(self, ctx: finalgrammarParser.Call_funcContext):

        self.tipo_call_func = ""

        self.num_param = 0
        if self.is_dep == False:
            self.aux_count = 0
            self.id_call_func = ""
        self.aux_func = ""
        self.is_dep = False
        self.aux_count2 = 0

    def exitListParam(self, ctx:finalgrammarParser.ListParamContext):
       pass

    def enterList_callf_param(self, ctx:finalgrammarParser.List_callf_paramContext):
        if self.is_dep == False:
            param = self.retorna_parametros_da_funcao(self.id_call_func)
        else:
            param = self.retorna_parametros_da_funcao(self.aux_func)

        num_fun = len(param)
        num_param = len(ctx.list_callf())

        if param != False:
            if num_fun != num_param:
                if self.is_dep == False:
                    raise Exception("O número de parametros passados a chamada da funçao " + self.id_call_func + " nao é compativel com a definiçao.")
                else:
                    raise Exception(
                        "O número de parametros passados a chamada da funçao " + self.aux_func + " nao é compativel com a definiçao.")

    def exitIgual(self, ctx:finalgrammarParser.IgualContext):
        self.text_file_out += f"\tif_icmpne L1\n"

    def exitDiferente(self, ctx:finalgrammarParser.DiferenteContext):
        self.text_file_out += f"\tif_icmpeq L1\n"

    def exitMaiorComp(self, ctx:finalgrammarParser.MaiorCompContext):
        self.text_file_out += f"\tif_icmple L1\n"

    def exitMenosComp(self, ctx:finalgrammarParser.MaiorCompContext):
        self.text_file_out += f"\tif_icmpge L1\n"

    def exitMaiorIgual(self, ctx:finalgrammarParser.MaiorIgualContext):
        self.text_file_out += f"\tif_icmplt L1\n"

    def exitMenorIgual(self, ctx:finalgrammarParser.MenorIgualContext):
        self.text_file_out += f"\tif_icmpgt L1\n"

    def enterIf_stm(self, ctx:finalgrammarParser.If_stmContext):
        pass

    def exitIf_stm(self, ctx:finalgrammarParser.If_stmContext):
        self.text_file_out += "\tL1: \n"

    def enterList_callf(self, ctx:finalgrammarParser.List_callfContext):
        if self.is_dep == False:
            param = self.retorna_parametros_da_funcao(self.id_call_func)
            tipo = param[self.aux_count]["TIPO"]
        else:
            param = self.retorna_parametros_da_funcao(self.aux_func)
            tipo = param[self.aux_count2]["TIPO"]

        if ctx.ID():

            id = ctx.ID().getText()
            tipo_local = self.retorna_tipo_da_variavel(id, str(self.escopo))
            tipo_global = self.retorna_tipo_da_variavel(id, "0")

            if tipo_local != "":
                if tipo_local != tipo:

                    raise Exception("O tipo da variavel passada como parametro nao existe1")
            elif tipo_global != "":
                if tipo_global != tipo:

                    raise Exception("O tipo da variavel passada como parametro nao existe2")
            else:
                raise Exception("A variável " + id + " nao existe.")

            if self.is_dep == False:
                self.aux_count = self.aux_count + 1
            else:
                self.aux_count2 = self.aux_count2 + 1

        elif ctx.BOOL():

            if tipo != "bool":
                raise Exception("O tipo da variavel passada como parametro nao existe3")

            if self.is_dep == False:
                self.aux_count = self.aux_count + 1
            else:
                self.aux_count2 = self.aux_count2 + 1

        elif ctx.STRING():

            if tipo != "String":
                raise Exception("O tipo da variavel passada como parametro nao existe")

            if self.is_dep == False:
                self.aux_count = self.aux_count + 1
            else:
                self.aux_count2 = self.aux_count2 + 1

        elif ctx.expression():
            self.tipo_expressao = tipo

            if self.is_dep == False:
                self.aux_count = self.aux_count + 1
            else:
                self.aux_count2 = self.aux_count2 + 1

        elif ctx.call_func():

            if self.is_dep == True:
                raise Exception("Só é permitido chamar uma funçao como parametro dentro de outra apenas umas vez no nível.")

            self.tipo_call_func = tipo
            self.aux_count = self.aux_count + 1
            self.is_dep = True




