grammar Expr;

root: expr EOF;

expr: expr (MAS | MENOS) expr
    | NUM
    ;

NUM   : [0-9]+ ;
MAS   : '+' ;
MENOS   : '-' ;
WS    : [ \n]+ -> skip ;