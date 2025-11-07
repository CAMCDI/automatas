# Generated from for.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .forParser import forParser
else:
    from forParser import forParser

# This class defines a complete listener for a parse tree produced by forParser.
class forListener(ParseTreeListener):

    # Enter a parse tree produced by forParser#programa.
    def enterPrograma(self, ctx:forParser.ProgramaContext):
        pass

    # Exit a parse tree produced by forParser#programa.
    def exitPrograma(self, ctx:forParser.ProgramaContext):
        pass


    # Enter a parse tree produced by forParser#sentencia.
    def enterSentencia(self, ctx:forParser.SentenciaContext):
        pass

    # Exit a parse tree produced by forParser#sentencia.
    def exitSentencia(self, ctx:forParser.SentenciaContext):
        pass


    # Enter a parse tree produced by forParser#asignacion.
    def enterAsignacion(self, ctx:forParser.AsignacionContext):
        pass

    # Exit a parse tree produced by forParser#asignacion.
    def exitAsignacion(self, ctx:forParser.AsignacionContext):
        pass


    # Enter a parse tree produced by forParser#condicional.
    def enterCondicional(self, ctx:forParser.CondicionalContext):
        pass

    # Exit a parse tree produced by forParser#condicional.
    def exitCondicional(self, ctx:forParser.CondicionalContext):
        pass


    # Enter a parse tree produced by forParser#bucleFor.
    def enterBucleFor(self, ctx:forParser.BucleForContext):
        pass

    # Exit a parse tree produced by forParser#bucleFor.
    def exitBucleFor(self, ctx:forParser.BucleForContext):
        pass


    # Enter a parse tree produced by forParser#condicion.
    def enterCondicion(self, ctx:forParser.CondicionContext):
        pass

    # Exit a parse tree produced by forParser#condicion.
    def exitCondicion(self, ctx:forParser.CondicionContext):
        pass


    # Enter a parse tree produced by forParser#expresion.
    def enterExpresion(self, ctx:forParser.ExpresionContext):
        pass

    # Exit a parse tree produced by forParser#expresion.
    def exitExpresion(self, ctx:forParser.ExpresionContext):
        pass


    # Enter a parse tree produced by forParser#termino.
    def enterTermino(self, ctx:forParser.TerminoContext):
        pass

    # Exit a parse tree produced by forParser#termino.
    def exitTermino(self, ctx:forParser.TerminoContext):
        pass


    # Enter a parse tree produced by forParser#factor.
    def enterFactor(self, ctx:forParser.FactorContext):
        pass

    # Exit a parse tree produced by forParser#factor.
    def exitFactor(self, ctx:forParser.FactorContext):
        pass



del forParser