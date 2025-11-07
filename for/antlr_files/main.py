import sys
from antlr4 import *
from forLexer import forLexer
from forParser import forParser
from forVisitor import forVisitor

class EvalVisitor(forVisitor):
    def __init__(self):
        self.variables = {}
    
    def visitPrograma(self, ctx):
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        return self.variables
    
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
        if isinstance(init_child, forParser.AsignacionContext):
            self.visit(init_child)
        elif isinstance(init_child, forParser.ExpresionContext):
            self.visit(init_child)
        
        cond_child = children[3]
        update_child = children[5] if len(children) > 5 else None
        
        max_iterations = 1000
        iteration = 0
        
        while iteration < max_iterations:
            iteration += 1
            
            if not self.visit(cond_child):
                break
            
            for sentencia in ctx.sentencia():
                self.visit(sentencia)
            
            if update_child:
                if isinstance(update_child, forParser.AsignacionContext):
                    self.visit(update_child)
                elif isinstance(update_child, forParser.ExpresionContext):
                    self.visit(update_child)
    
    def visitCondicional(self, ctx):
        if self.visit(ctx.condicion()):
            for sentencia in ctx.sentencia():
                self.visit(sentencia)

def main():
    print("Ingresa código con for: ", end="")
    input_stream = InputStream(input())
    
    lexer = forLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = forParser(stream)
    tree = parser.programa()
    
    visitor = EvalVisitor()
    result = visitor.visitPrograma(tree)
    print(result)

if __name__ == '__main__':
    main()