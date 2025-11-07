# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#programa.
    def visitPrograma(self, ctx:CalculadoraParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#sentencia.
    def visitSentencia(self, ctx:CalculadoraParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#asignacion.
    def visitAsignacion(self, ctx:CalculadoraParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#condicional.
    def visitCondicional(self, ctx:CalculadoraParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#condicion.
    def visitCondicion(self, ctx:CalculadoraParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#expresion.
    def visitExpresion(self, ctx:CalculadoraParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#termino.
    def visitTermino(self, ctx:CalculadoraParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#factor.
    def visitFactor(self, ctx:CalculadoraParser.FactorContext):
        return self.visitChildren(ctx)



del CalculadoraParser