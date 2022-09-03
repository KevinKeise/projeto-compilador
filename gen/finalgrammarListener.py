# Generated from C:/Users/kevin/OneDrive/Área de Trabalho/trabalho-final\finalgrammar.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .finalgrammarParser import finalgrammarParser
else:
    from finalgrammarParser import finalgrammarParser

# This class defines a complete listener for a parse tree produced by finalgrammarParser.
class finalgrammarListener(ParseTreeListener):

    # Enter a parse tree produced by finalgrammarParser#programa.
    def enterPrograma(self, ctx:finalgrammarParser.ProgramaContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#programa.
    def exitPrograma(self, ctx:finalgrammarParser.ProgramaContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#decVar.
    def enterDecVar(self, ctx:finalgrammarParser.DecVarContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#decVar.
    def exitDecVar(self, ctx:finalgrammarParser.DecVarContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#sm_dec_var.
    def enterSm_dec_var(self, ctx:finalgrammarParser.Sm_dec_varContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#sm_dec_var.
    def exitSm_dec_var(self, ctx:finalgrammarParser.Sm_dec_varContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#att_dec_var.
    def enterAtt_dec_var(self, ctx:finalgrammarParser.Att_dec_varContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#att_dec_var.
    def exitAtt_dec_var(self, ctx:finalgrammarParser.Att_dec_varContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#list_att.
    def enterList_att(self, ctx:finalgrammarParser.List_attContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#list_att.
    def exitList_att(self, ctx:finalgrammarParser.List_attContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#att.
    def enterAtt(self, ctx:finalgrammarParser.AttContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#att.
    def exitAtt(self, ctx:finalgrammarParser.AttContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#att_e.
    def enterAtt_e(self, ctx:finalgrammarParser.Att_eContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#att_e.
    def exitAtt_e(self, ctx:finalgrammarParser.Att_eContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#att_s.
    def enterAtt_s(self, ctx:finalgrammarParser.Att_sContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#att_s.
    def exitAtt_s(self, ctx:finalgrammarParser.Att_sContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#att_m.
    def enterAtt_m(self, ctx:finalgrammarParser.Att_mContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#att_m.
    def exitAtt_m(self, ctx:finalgrammarParser.Att_mContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#expression.
    def enterExpression(self, ctx:finalgrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#expression.
    def exitExpression(self, ctx:finalgrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#Soma.
    def enterSoma(self, ctx:finalgrammarParser.SomaContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#Soma.
    def exitSoma(self, ctx:finalgrammarParser.SomaContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#ExprTerm.
    def enterExprTerm(self, ctx:finalgrammarParser.ExprTermContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#ExprTerm.
    def exitExprTerm(self, ctx:finalgrammarParser.ExprTermContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#Subtracao.
    def enterSubtracao(self, ctx:finalgrammarParser.SubtracaoContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#Subtracao.
    def exitSubtracao(self, ctx:finalgrammarParser.SubtracaoContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#Div.
    def enterDiv(self, ctx:finalgrammarParser.DivContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#Div.
    def exitDiv(self, ctx:finalgrammarParser.DivContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#TermFactor.
    def enterTermFactor(self, ctx:finalgrammarParser.TermFactorContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#TermFactor.
    def exitTermFactor(self, ctx:finalgrammarParser.TermFactorContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#Multi.
    def enterMulti(self, ctx:finalgrammarParser.MultiContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#Multi.
    def exitMulti(self, ctx:finalgrammarParser.MultiContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#ParentesesArit.
    def enterParentesesArit(self, ctx:finalgrammarParser.ParentesesAritContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#ParentesesArit.
    def exitParentesesArit(self, ctx:finalgrammarParser.ParentesesAritContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#InteiroAri.
    def enterInteiroAri(self, ctx:finalgrammarParser.InteiroAriContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#InteiroAri.
    def exitInteiroAri(self, ctx:finalgrammarParser.InteiroAriContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#IdAri.
    def enterIdAri(self, ctx:finalgrammarParser.IdAriContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#IdAri.
    def exitIdAri(self, ctx:finalgrammarParser.IdAriContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#RealAri.
    def enterRealAri(self, ctx:finalgrammarParser.RealAriContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#RealAri.
    def exitRealAri(self, ctx:finalgrammarParser.RealAriContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#CallFuncAri.
    def enterCallFuncAri(self, ctx:finalgrammarParser.CallFuncAriContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#CallFuncAri.
    def exitCallFuncAri(self, ctx:finalgrammarParser.CallFuncAriContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#MenosUnarioAri.
    def enterMenosUnarioAri(self, ctx:finalgrammarParser.MenosUnarioAriContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#MenosUnarioAri.
    def exitMenosUnarioAri(self, ctx:finalgrammarParser.MenosUnarioAriContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#teste_comp.
    def enterTeste_comp(self, ctx:finalgrammarParser.Teste_compContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#teste_comp.
    def exitTeste_comp(self, ctx:finalgrammarParser.Teste_compContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#Igual.
    def enterIgual(self, ctx:finalgrammarParser.IgualContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#Igual.
    def exitIgual(self, ctx:finalgrammarParser.IgualContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#TermComp.
    def enterTermComp(self, ctx:finalgrammarParser.TermCompContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#TermComp.
    def exitTermComp(self, ctx:finalgrammarParser.TermCompContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#Diferente.
    def enterDiferente(self, ctx:finalgrammarParser.DiferenteContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#Diferente.
    def exitDiferente(self, ctx:finalgrammarParser.DiferenteContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#MenorIgual.
    def enterMenorIgual(self, ctx:finalgrammarParser.MenorIgualContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#MenorIgual.
    def exitMenorIgual(self, ctx:finalgrammarParser.MenorIgualContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#MaiorComp.
    def enterMaiorComp(self, ctx:finalgrammarParser.MaiorCompContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#MaiorComp.
    def exitMaiorComp(self, ctx:finalgrammarParser.MaiorCompContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#MenosComp.
    def enterMenosComp(self, ctx:finalgrammarParser.MenosCompContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#MenosComp.
    def exitMenosComp(self, ctx:finalgrammarParser.MenosCompContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#MaiorIgual.
    def enterMaiorIgual(self, ctx:finalgrammarParser.MaiorIgualContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#MaiorIgual.
    def exitMaiorIgual(self, ctx:finalgrammarParser.MaiorIgualContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#ExprBool.
    def enterExprBool(self, ctx:finalgrammarParser.ExprBoolContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#ExprBool.
    def exitExprBool(self, ctx:finalgrammarParser.ExprBoolContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#TermBool.
    def enterTermBool(self, ctx:finalgrammarParser.TermBoolContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#TermBool.
    def exitTermBool(self, ctx:finalgrammarParser.TermBoolContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#AndOp.
    def enterAndOp(self, ctx:finalgrammarParser.AndOpContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#AndOp.
    def exitAndOp(self, ctx:finalgrammarParser.AndOpContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#OuOp.
    def enterOuOp(self, ctx:finalgrammarParser.OuOpContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#OuOp.
    def exitOuOp(self, ctx:finalgrammarParser.OuOpContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactComp.
    def enterFactComp(self, ctx:finalgrammarParser.FactCompContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactComp.
    def exitFactComp(self, ctx:finalgrammarParser.FactCompContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactPar.
    def enterFactPar(self, ctx:finalgrammarParser.FactParContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactPar.
    def exitFactPar(self, ctx:finalgrammarParser.FactParContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactInt.
    def enterFactInt(self, ctx:finalgrammarParser.FactIntContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactInt.
    def exitFactInt(self, ctx:finalgrammarParser.FactIntContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactReal.
    def enterFactReal(self, ctx:finalgrammarParser.FactRealContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactReal.
    def exitFactReal(self, ctx:finalgrammarParser.FactRealContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactString.
    def enterFactString(self, ctx:finalgrammarParser.FactStringContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactString.
    def exitFactString(self, ctx:finalgrammarParser.FactStringContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactBool.
    def enterFactBool(self, ctx:finalgrammarParser.FactBoolContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactBool.
    def exitFactBool(self, ctx:finalgrammarParser.FactBoolContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactId.
    def enterFactId(self, ctx:finalgrammarParser.FactIdContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactId.
    def exitFactId(self, ctx:finalgrammarParser.FactIdContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactExpression.
    def enterFactExpression(self, ctx:finalgrammarParser.FactExpressionContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactExpression.
    def exitFactExpression(self, ctx:finalgrammarParser.FactExpressionContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#FactNot.
    def enterFactNot(self, ctx:finalgrammarParser.FactNotContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#FactNot.
    def exitFactNot(self, ctx:finalgrammarParser.FactNotContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#function.
    def enterFunction(self, ctx:finalgrammarParser.FunctionContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#function.
    def exitFunction(self, ctx:finalgrammarParser.FunctionContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#main_function.
    def enterMain_function(self, ctx:finalgrammarParser.Main_functionContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#main_function.
    def exitMain_function(self, ctx:finalgrammarParser.Main_functionContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#listParam.
    def enterListParam(self, ctx:finalgrammarParser.ListParamContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#listParam.
    def exitListParam(self, ctx:finalgrammarParser.ListParamContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#call_func.
    def enterCall_func(self, ctx:finalgrammarParser.Call_funcContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#call_func.
    def exitCall_func(self, ctx:finalgrammarParser.Call_funcContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#list_callf_param.
    def enterList_callf_param(self, ctx:finalgrammarParser.List_callf_paramContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#list_callf_param.
    def exitList_callf_param(self, ctx:finalgrammarParser.List_callf_paramContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#IdParametroFunc.
    def enterIdParametroFunc(self, ctx:finalgrammarParser.IdParametroFuncContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#IdParametroFunc.
    def exitIdParametroFunc(self, ctx:finalgrammarParser.IdParametroFuncContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#CallFuncParametroFunc.
    def enterCallFuncParametroFunc(self, ctx:finalgrammarParser.CallFuncParametroFuncContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#CallFuncParametroFunc.
    def exitCallFuncParametroFunc(self, ctx:finalgrammarParser.CallFuncParametroFuncContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#ExpressionParametroFunc.
    def enterExpressionParametroFunc(self, ctx:finalgrammarParser.ExpressionParametroFuncContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#ExpressionParametroFunc.
    def exitExpressionParametroFunc(self, ctx:finalgrammarParser.ExpressionParametroFuncContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#return_stm.
    def enterReturn_stm(self, ctx:finalgrammarParser.Return_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#return_stm.
    def exitReturn_stm(self, ctx:finalgrammarParser.Return_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#print_stm.
    def enterPrint_stm(self, ctx:finalgrammarParser.Print_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#print_stm.
    def exitPrint_stm(self, ctx:finalgrammarParser.Print_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#list_p.
    def enterList_p(self, ctx:finalgrammarParser.List_pContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#list_p.
    def exitList_p(self, ctx:finalgrammarParser.List_pContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#list_sv.
    def enterList_sv(self, ctx:finalgrammarParser.List_svContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#list_sv.
    def exitList_sv(self, ctx:finalgrammarParser.List_svContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#input_stm.
    def enterInput_stm(self, ctx:finalgrammarParser.Input_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#input_stm.
    def exitInput_stm(self, ctx:finalgrammarParser.Input_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#if_stm.
    def enterIf_stm(self, ctx:finalgrammarParser.If_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#if_stm.
    def exitIf_stm(self, ctx:finalgrammarParser.If_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#for_stm.
    def enterFor_stm(self, ctx:finalgrammarParser.For_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#for_stm.
    def exitFor_stm(self, ctx:finalgrammarParser.For_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#do_while_stm.
    def enterDo_while_stm(self, ctx:finalgrammarParser.Do_while_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#do_while_stm.
    def exitDo_while_stm(self, ctx:finalgrammarParser.Do_while_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#f_stm.
    def enterF_stm(self, ctx:finalgrammarParser.F_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#f_stm.
    def exitF_stm(self, ctx:finalgrammarParser.F_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#s_stm.
    def enterS_stm(self, ctx:finalgrammarParser.S_stmContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#s_stm.
    def exitS_stm(self, ctx:finalgrammarParser.S_stmContext):
        pass


    # Enter a parse tree produced by finalgrammarParser#blocks.
    def enterBlocks(self, ctx:finalgrammarParser.BlocksContext):
        pass

    # Exit a parse tree produced by finalgrammarParser#blocks.
    def exitBlocks(self, ctx:finalgrammarParser.BlocksContext):
        pass



del finalgrammarParser