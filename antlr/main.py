from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser
from EvalVisitor import EvalVisitor

def evaluate_expression(expr: str):
    # Crear el flujo de entrada
    input_stream = InputStream(expr)
    lexer = ArithmeticLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ArithmeticParser(token_stream)
    
    # Parsear la expresion
    tree = parser.expr()

    #Visitor
    visitor = EvalVisitor()
    result = visitor.visit(tree)
    return result

# probar ejemplos
examples = ["3+2", "7-4", "2*3", "8/2", "9/0"]
for e in examples:
        try:
            print(f"{e} = {evaluate_expression(e)}")
        except Exception as ex:
            print(f"{e} -> {ex}")
