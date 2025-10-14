from antlr4 import InputStream, CommonTokenStream
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser

def test_expression(input_expr):
    # Crear flujo de entrada
    input_stream = InputStream(input_expr)
    # Lexer
    lexer = ArithmeticLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    # Parser
    parser = ArithmeticParser(token_stream) 
    tree = parser.expr()
    # Mostrar árbol sintáctico
    print(f"Entrada: {input_expr}")
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    # Pedir al usuario que escriba una expresión
    expr = input("Escribe una expresión aritmética: ")
    test_expression(expr)




