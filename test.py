from antlr4 import * #Exportar paquetes
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

input_stream = InputStream(input('?'))
lexer = ExprLexer(input_stream) #Reglas de contruccion
token_stream = CommonTokenStream(lexer) #conevrtir a flujo de tokens, convertir lexico a flujo de tokens
parser = ExprParser(token_stream) #Se esta convietiendo en lo que nosotros deseamos (token)
tree = parser.root() #Esperando respuesta

visitor = ExprVisitor()
visitor.visit(tree)


# Abstract Systax Tree / Arbol de Sintaxis Abstracta (ATS)
# sizeof almacena el tamaño de la variable
# malooc 
