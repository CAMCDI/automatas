from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from antlr4 import *
from MiniLangLexer import MiniLangLexer
from MiniLangParser import MiniLangParser
from EvalVisitor import EvalVisitor

app = FastAPI()

def evaluate_expression(code: str):
    input_stream = InputStream(code)
    lexer = MiniLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniLangParser(token_stream)
    tree = parser.program()
    visitor = EvalVisitor()
    return visitor.visit(tree)

@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
def index(x: int = Form(None), y: int = Form(None)):
    result = ""
    if x is not None and y is not None:
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

   
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    html = html.replace("{% if result %}", "")
    html = html.replace("{{ result }}", result)
    html = html.replace("{% endif %}", "")
    return HTMLResponse(html)
