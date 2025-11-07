grammar for;

FOR: 'for';
IF: 'if';
PRINT: 'print';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUM: [0-9]+;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;

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

programa: sentencia* EOF;

sentencia: asignacion
         | condicional
         | bucleFor
         | print
         | expresion SEMI
         ;

asignacion: ID ASSIGN expresion SEMI;

condicional: IF LPAREN condicion RPAREN LBRACE sentencia* RBRACE;

bucleFor: FOR LPAREN (asignacion | expresion? SEMI) condicion SEMI (asignacion | expresion)? RPAREN LBRACE sentencia* RBRACE;

print: PRINT expresion SEMI;

condicion: expresion (GT | LT | EQ | NEQ) expresion;

expresion: termino ((PLUS | MINUS) termino)*;

termino: factor ((MULT | DIV) factor)*;

factor: NUM | ID | STRING | LPAREN expresion RPAREN;