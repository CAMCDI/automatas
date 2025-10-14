grammar Arithmetic;

//Regla inicial
expr:DIGIT OP DIGIT EOF;

//Tokens
DIGIT:[0-9];
OP :'+'|'-'|'*'|'/';

//Ignorar espacios

WS:[\t\r\n]+-> skip;