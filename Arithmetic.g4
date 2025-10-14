grammar Arithmetic;

expr : DIGIT OP DIGIT EOF ;

DIGIT : [0-9] ;
OP    : '+'|'-'|'*'|'/' ;

WS :[ \t\r\n] + -> skip ;