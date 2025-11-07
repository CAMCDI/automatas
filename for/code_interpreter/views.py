import sys
import os
from django.shortcuts import render
from django.http import JsonResponse

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'antlr_files'))

from antlr4 import *
from forLexer import forLexer
from forParser import forParser
from forVisitor import forVisitor

class EvalVisitor(forVisitor):
    def __init__(self):
        self.variables = {}
        self.iterations = []
        self.current_iteration = 0
        self.output = []  
    
    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.variables
    
    def visitSentencia(self, ctx):
        return self.visitChildren(ctx)
    
    # ← NUEVO: Manejar print
    def visitPrint(self, ctx):
        value = self.visit(ctx.expresion())
        self.output.append(str(value)) 
        return value
    
    def visitAsignacion(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var_name] = value
        return value
    
    def visitExpresion(self, ctx):
        if len(ctx.termino()) == 1 and not ctx.PLUS() and not ctx.MINUS():
            return self.visit(ctx.termino(0))
        
        result = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.termino(i))
            if op == '+':
                result += right
            elif op == '-':
                result -= right
        return result
    
    def visitTermino(self, ctx):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2*i - 1).getText()
            right = self.visit(ctx.factor(i))
            if op == '*':
                result *= right
            elif op == '/':
                result //= right
        return result
    
    def visitFactor(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            return self.variables.get(var_name, 0)
        elif ctx.expresion():
            return self.visit(ctx.expresion())
        return 0
    
    def visitCondicion(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        
        if op == '>':
            return left > right
        elif op == '<':
            return left < right
        elif op == '==':
            return left == right
        elif op == '!=':
            return left != right
        return False
    
    def visitBucleFor(self, ctx):
        children = list(ctx.getChildren())
        
        init_child = children[2]
        if hasattr(init_child, 'accept'):
            self.visit(init_child)
        
        cond_child = children[3]
        update_child = children[5] if len(children) > 5 else None
        
        max_iterations = 1000
        iteration_count = 0
        
        while iteration_count < max_iterations:
            iteration_count += 1
            self.current_iteration = iteration_count
            
            condition_result = self.visit(cond_child)
            
            iteration_info = {
                'numero': iteration_count,
                'condicion': f"{cond_child.getText()} = {condition_result}",
                'variables_antes': self.variables.copy(),
                'ejecutado': condition_result
            }
            
            if not condition_result:
                iteration_info['mensaje'] = 'Condición falsa - fin del bucle'
                self.iterations.append(iteration_info)
                break
            
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
            
            iteration_info['variables_despues'] = self.variables.copy()
            self.iterations.append(iteration_info)
            
            if update_child and hasattr(update_child, 'accept'):
                self.visit(update_child)
    
    def visitCondicional(self, ctx):
        if self.visit(ctx.condicion()):
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
    
    def visitChildren(self, ctx):
        for child in ctx.getChildren():
            if hasattr(child, 'accept'):
                child.accept(self)
        return None

def index(request):
    return render(request, 'code_interpreter/index.html')

def execute_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        
        try:
            input_stream = InputStream(code)
            lexer = forLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = forParser(stream)
            tree = parser.programa()
            
            visitor = EvalVisitor()
            result = visitor.visitPrograma(tree)
            
            return render(request, 'code_interpreter/result.html', {
                'code': code,
                'result': result,
                'iterations': visitor.iterations,
                'output': visitor.output, 
                'success': True
            })
            
        except Exception as e:
            return render(request, 'code_interpreter/result.html', {
                'code': code,
                'error': str(e),
                'success': False
            })
    
    return render(request, 'code_interpreter/index.html')