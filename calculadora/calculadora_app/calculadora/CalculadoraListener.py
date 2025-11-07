# Generated from Calculadora.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete listener for a parse tree produced by CalculadoraParser.
class CalculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraParser#programa.
    def enterPrograma(self, ctx:CalculadoraParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#programa.
    def exitPrograma(self, ctx:CalculadoraParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#sentencia.
    def enterSentencia(self, ctx:CalculadoraParser.SentenciaContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#sentencia.
    def exitSentencia(self, ctx:CalculadoraParser.SentenciaContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#asignacion.
    def enterAsignacion(self, ctx:CalculadoraParser.AsignacionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#asignacion.
    def exitAsignacion(self, ctx:CalculadoraParser.AsignacionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#condicional.
    def enterCondicional(self, ctx:CalculadoraParser.CondicionalContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#condicional.
    def exitCondicional(self, ctx:CalculadoraParser.CondicionalContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#condicion.
    def enterCondicion(self, ctx:CalculadoraParser.CondicionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#condicion.
    def exitCondicion(self, ctx:CalculadoraParser.CondicionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#expresion.
    def enterExpresion(self, ctx:CalculadoraParser.ExpresionContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#expresion.
    def exitExpresion(self, ctx:CalculadoraParser.ExpresionContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#termino.
    def enterTermino(self, ctx:CalculadoraParser.TerminoContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#termino.
    def exitTermino(self, ctx:CalculadoraParser.TerminoContext):
        pass


    # Enter a parse tree produced by CalculadoraParser#factor.
    def enterFactor(self, ctx:CalculadoraParser.FactorContext):
        pass

    # Exit a parse tree produced by CalculadoraParser#factor.
    def exitFactor(self, ctx:CalculadoraParser.FactorContext):
        pass



del CalculadoraParser