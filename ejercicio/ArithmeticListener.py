# Generated from Arithmetic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ArithmeticParser import ArithmeticParser
else:
    from ArithmeticParser import ArithmeticParser

# This class defines a complete listener for a parse tree produced by ArithmeticParser.
class ArithmeticListener(ParseTreeListener):

    # Enter a parse tree produced by ArithmeticParser#expr.
    def enterExpr(self, ctx:ArithmeticParser.ExprContext):
        pass

    # Exit a parse tree produced by ArithmeticParser#expr.
    def exitExpr(self, ctx:ArithmeticParser.ExprContext):
        pass



del ArithmeticParser