grammar finalgrammar;

programa: initial_vars function* main_function;

// variaveis

initial_vars: decVar*;

decVar: sm_dec_var      // declara variaveis sem inicializa-las
      | att_dec_var  //declara variaveis inicializando-as
      ;

sm_dec_var: TIPO ID (',' ID)* ';'; // int var1,var2,...,varn;

att_dec_var: TIPO ID '=' (STRING | REAL | BOOL | INT) (',' ID '=' (STRING | REAL | BOOL | INT))* ';'; //int var1=1,var2=2,...,varn=98;

list_att: att (',' att)*;

// Atribuiçao
att : ID '=' (STRING | REAL | BOOL | INT);  // ex: var = 34
att_e : ID '=' (expression | STRING | BOOL);  // ex: var = 34+5
att_s : ID '+=' (REAL | INT | ID);
att_m : ID '*=' (REAL | INT | ID);

//expressoes aritmeticas

expression : expr_id | expr_int | expr_real;

expr_int: expr_int '+' term_int #IntSoma
        | expr_int '-' term_int #IntSubtracao
        | term_int  #IntExprTerm
        ;

term_int: term_int '*' factor_int #IntMulti
        | term_int '/' factor_int #IntDiv
        | factor_int #IntTermFactor
        ;

factor_int: '(' expr_int ')' #IntParentesesArit
      | INT #IntInteiroAri
      | ID #IntIdAri
      | call_func #IntCallFuncAri
      | '-' factor_int #IntMenosUnarioAri
      ;

expr_real: expr_real '+' term_real #RealSoma
         | expr_real '-' term_real #RealSubtracao
         | term_real  #RealExprTerm
         ;

term_real: term_real '*' factor_real #RealMulti
         | term_real '/' factor_real #RealDiv
         | factor_real #RealTermFactor
         ;

factor_real: '(' expr_real ')' #RealParentesesArit
      | REAL #RealAri
      | ID #RealIdAri
      | call_func #RealCallFuncAri
      | '-' factor_real #RealMenosUnarioAri
      ;

expr_id: expr_id '+' term_id #IdSoma
         | expr_id '-' term_id #IdSubtracao
         | term_id  #IdExprTerm
         ;

term_id: term_id '*' factor_id #IdMulti
         | term_id '/' factor_id #IdDiv
         | factor_id #IdTermFactor
         ;

factor_id: '(' expr_id ')' #IdParentesesArit
      | ID #IdIdAri
      | call_func #IdCallFuncAri
      | '-' factor_id #IdMenosUnarioAri
      ;

// expressoes de comparaçao

teste_comp: expr_comp;

expr_comp: expr_comp '==' term_comp #Igual
         | expr_comp '!=' term_comp #Diferente
         | term_comp #TermComp
         ;

term_comp: term_comp '>=' expr_bool #MaiorIgual
         | term_comp '<=' expr_bool #MenorIgual
         | term_comp '>' expr_bool #MaiorComp
         | term_comp '<' expr_bool #MenosComp
         | expr_bool #ExprBool
         ;

expr_bool: expr_bool '&&' term_bool #AndOp
         | term_bool #TermBool
         ;

term_bool: term_bool '||' fact_comp #OuOp
         | fact_comp #FactComp
         ;

fact_comp: '(' expr_comp ')'
         | STRING
         | BOOL
         | ID
         | expression
         |  '!' fact_comp
         ;


// funçoes

function : 'def' ID '(' listParam* ')' TIPO '{' initial_vars blocks* '}'; // define uma funçao qualquer

main_function : 'def' 'main' '(' listParam* ')' '{' initial_vars blocks+ '}'; // define a funçao principal

listParam: TIPO ID (',' TIPO ID)* ; // lista de parametros da funçao

call_func: ID '('list_callf_param*')'; // define como se chama uma funçao sem ponto e virgula

list_callf_param: list_callf (',' list_callf)*;
// define os tipos de parametro de uma funçao Ex: func(3+2) ou func(var) etc...
list_callf: call_func
          | STRING
          | BOOL
          | ID
          | expression
          ;

return_stm: 'return' (ID | BOOL | STRING | expression | call_func | teste_comp) ';'; // define o 'return' da funçao

//print

print_stm: 'print' '(' list_p+ ')' ';';

list_p: list_sv (',' list_sv)*;

list_sv: STRING #PrintString
       | ID #PrintId
       | expression #PrintExpression
       | call_func #PrintFunc
       ;
//input

input_stm: ID '=' 'input()' ';'; // define o input

// if-else

if_stm: 'if' '(' teste_comp  ')' '{' blocks* '}' ('else' '{' blocks+ '}')?;

//for

for_stm: 'for' ID 'in' 'range' '(' (INT | ID) ':' (INT | ID) (':' (INT | ID))? ')' '{' blocks+ '}';

//do-while

do_while_stm : 'do' '{' blocks+  '}' 'while' '(' teste_comp ')' ';';

//blocos
f_stm: for_stm
     | do_while_stm
     | if_stm
     ;

s_stm: call_func ';'
     | att_e ';'
     | att_m ';'
     | att_s ';'
     | return_stm
     | print_stm
     | input_stm
     | BREAK
     ;


blocks: s_stm | f_stm;

TIPO: 'int' | 'real' | 'bool' | 'String' | 'void';
fragment DIGIT: [0-9];
BOOL: 'True' | 'False';
BREAK: 'break';
INT: DIGIT+;
REAL: DIGIT+ '.' DIGIT+ ;
COMP: '==' | '!=' | '>=' | '<=' | '>' | '<';
STRING: '"' .*? '"';
ID: [a-zA-Z1-9]+;
WS : [ \t\r\n]+ -> skip ;