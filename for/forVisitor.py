# Generated from for.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .forParser import forParser
else:
    from forParser import forParser

# This class defines a complete generic visitor for a parse tree produced by forParser.

class forVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by forParser#programa.
    def visitPrograma(self, ctx:forParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#sentencia.
    def visitSentencia(self, ctx:forParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#asignacion.
    def visitAsignacion(self, ctx:forParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#condicional.
    def visitCondicional(self, ctx:forParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#bucleFor.
    def visitBucleFor(self, ctx:forParser.BucleForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#condicion.
    def visitCondicion(self, ctx:forParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#expresion.
    def visitExpresion(self, ctx:forParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#termino.
    def visitTermino(self, ctx:forParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by forParser#factor.
    def visitFactor(self, ctx:forParser.FactorContext):
        return self.visitChildren(ctx)



del forParser