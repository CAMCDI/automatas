from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from antlr4 import *
from .MiniLangLexer import MiniLangLexer
from .MiniLangParser import MiniLangParser
from .EvalVisitor import EvalVisitor

def evaluate_expression(code: str):
    input_stream = InputStream(code)
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)
    tree = parser.program()
    visitor = EvalVisitor()
    return visitor.visit(tree)

@csrf_exempt  # quitar esto si quieres seguridad CSRF en producción
def index(request):
    result = ""
    if request.method == "POST":
        x = request.POST.get("x")
        y = request.POST.get("y")
        if x and y:
            user_code = (
                f"x = {x}\n"
                f"y = {y}\n"
                f"z = x * y + 10\n"
                f"print(z)\n"
                f"x = x + 1\n"
                f"print(x)\n"
            )
            try:
                result = evaluate_expression(user_code)
            except Exception as ex:
                result = f"Error: {ex}"
    return render(request, "index.html", {"result": result})
