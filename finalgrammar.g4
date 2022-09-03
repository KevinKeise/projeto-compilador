grammar finalgrammar;

programa: decVar* function* main_function;

// variaveis

decVar: sm_dec_var      // declara variaveis sem inicializa-las
      | att_dec_var  //declara variaveis inicializando-as
      ;

sm_dec_var: TIPO ID (',' ID)* ';'; // int var1,var2,...,varn;

att_dec_var: TIPO ID '=' (STRING | REAL | BOOL | INT) (',' ID '=' (STRING | REAL | BOOL | INT))* ';'; //int var1=1,var2=2,...,varn=98;

list_att: att (',' att)*;

// Atribuiçao
att : ID '=' (STRING | REAL | BOOL | INT);  // ex: var = 34
att_e : ID '=' (expression | STRING | BOOL );  // ex: var = 34+5
att_s : ID '+=' (STRING | REAL | BOOL | INT);
att_m : ID '*=' (STRING | REAL | BOOL | INT);
//expressoes aritmeticas

expression returns [int val]: expr;

expr returns [int val]:
      expr '+' term #Soma
    | expr '-' term #Subtracao
    | term  #ExprTerm
    ;

term returns [int val]:
    term '*' factor #Multi
    | term '/' factor #Div
    | factor #TermFactor
    ;

factor returns [int val]: '(' expr ')' #ParentesesArit
      | INT #InteiroAri
      | ID #IdAri
      | REAL #RealAri
      | call_func #CallFuncAri
      | '-' factor #MenosUnarioAri
      ;

// expressoes de comparaçao

teste_comp: expr_comp;

expr_comp returns [int val]: expr_comp '==' term_comp #Igual
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

fact_comp: '(' expr_comp ')' #FactPar
         | INT #FactInt
         | REAL #FactReal
         | STRING #FactString
         | BOOL #FactBool
         | ID #FactId
         | expression #FactExpression
         |  '!' fact_comp #FactNot
         ;


// funçoes

function : 'def' ID '(' listParam* ')' TIPO '{' decVar* blocks* '}'; // define uma funçao qualquer

main_function : 'def' 'main' '(' listParam* ')' '{' decVar* blocks+ '}'; // define a funçao principal

listParam: TIPO ID (',' TIPO ID)* ; // lista de parametros da funçao

call_func: ID '('list_callf_param*')'; // define como se chama uma funçao sem ponto e virgula

list_callf_param: list_callf (',' list_callf)*;
// define os tipos de parametro de uma funçao Ex: func(3+2) ou func(var) etc...
list_callf: ID  #IdParametroFunc
          | call_func #CallFuncParametroFunc
          | expression #ExpressionParametroFunc
          ;

return_stm: 'return' (ID | BOOL | expression | call_func) ';'; // define o 'return' da funçao

//print

print_stm: 'print' '(' list_p+ ')' ';';

list_p: list_sv (',' list_sv)*;

list_sv: STRING
       | ID
       | expression
       | call_func
       ;
//input

input_stm: ID '=' 'input()' ';'; // define o input

// if-else

if_stm: 'if' '(' teste_comp  ')' '{' blocks* '}' ('else' '{' blocks+ '}')?;

//for

for_stm: 'for' ID 'in' 'range' '(' INT ':' INT (':' INT)? ')' '{' blocks+ '}';

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