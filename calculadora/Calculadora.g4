grammar Calculadora;

// Reglas léxicas
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;

// Operadores y símbolos
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
GT: '>';
LT: '<';
EQ: '==';
NEQ: '!=';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';

// Reglas sintácticas
programa: sentencia*;

sentencia: asignacion | condicional | expresion SEMI;

asignacion: ID ASSIGN expresion SEMI;

condicional: 'if' LPAREN condicion RPAREN LBRACE sentencia* RBRACE;

condicion: expresion (GT | LT | EQ | NEQ) expresion;

expresion: termino ( (PLUS | MINUS) termino )*;

termino: factor ( (MULT | DIV) factor )*;

factor: NUM | ID | LPAREN expresion RPAREN;