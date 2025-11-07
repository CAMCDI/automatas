from antlr4 import *
from CalculadoraLexer import CalculadoraLexer
from CalculadoraParser import CalculadoraParser
from CalculadoraVisitor import CalculadoraVisitor

class MiCalculadoraVisitor(CalculadoraVisitor):
    def __init__(self):
        self.variables = {}
        self.pasos = []  # Lista para almacenar los pasos
        self.paso_numero = 1
        super().__init__()
    
    def agregar_paso(self, descripcion):
        self.pasos.append(f"Paso {self.paso_numero}: {descripcion}")
        self.paso_numero += 1
    
    def visitPrograma(self, ctx):
        self.agregar_paso("Inicio del programa")
        for sentencia in ctx.sentencia():
            self.visit(sentencia)
        self.agregar_paso("Fin del programa")
        return self.variables
    
    def visitAsignacion(self, ctx):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expresion())
        self.variables[var_name] = value
        
        descripcion = f"Asignación: {var_name} = {value}"
        estado = f"Estado de variables: {self.variables}"
        self.agregar_paso(f"{descripcion}. {estado}")
        
        return value
    
    def visitCondicional(self, ctx):
        condicion_texto = ctx.condicion().getText()
        self.agregar_paso(f"Inicio condicional: if ({condicion_texto})")
        
        condition_result = self.visit(ctx.condicion())
        
        if condition_result:
            self.agregar_paso(f"Condición ({condicion_texto}) es VERDADERA - Ejecutando bloque IF")
            for stmt in ctx.sentencia():
                self.visit(stmt)
        else:
            self.agregar_paso(f"Condición ({condicion_texto}) es FALSA - Saltando bloque IF")
        
        return None
    
    def visitCondicion(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        
        if op == '>': 
            resultado = left > right
        elif op == '<': 
            resultado = left < right
        elif op == '==': 
            resultado = left == right
        elif op == '!=': 
            resultado = left != right
        
        self.agregar_paso(f"Evaluando condición: {left} {op} {right} = {resultado}")
        return resultado
    
    def visitExpresion(self, ctx):
        result = self.visit(ctx.termino(0))
        
        for i in range(1, len(ctx.termino())):
            op = ctx.getChild(2 * i - 1).getText()
            term_val = self.visit(ctx.termino(i))
            
            if op == '+': 
                result += term_val
            elif op == '-': 
                result -= term_val
        
        return result
    
    def visitTermino(self, ctx):
        result = self.visit(ctx.factor(0))
        
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(2 * i - 1).getText()
            factor_val = self.visit(ctx.factor(i))
            
            if op == '*': 
                result *= factor_val
            elif op == '/': 
                if factor_val == 0:
                    raise ValueError("Division por cero")
                result //= factor_val
        
        return result
    
    def visitFactor(self, ctx):
        if ctx.NUM():
            return int(ctx.NUM().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            else:
                raise NameError(f"Variable no definida: {var_name}")
        elif ctx.expresion():
            return self.visit(ctx.expresion())