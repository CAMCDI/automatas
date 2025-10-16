# Generated from Arithmetic.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,8,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,6,0,2,1,0,0,
        0,2,3,5,1,0,0,3,4,5,2,0,0,4,5,5,1,0,0,5,6,5,0,0,1,6,1,1,0,0,0,0
    ]

class ArithmeticParser ( Parser ):

    grammarFileName = "Arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "DIGIT", "OP", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    DIGIT=1
    OP=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticParser.DIGIT)
            else:
                return self.getToken(ArithmeticParser.DIGIT, i)

        def OP(self):
            return self.getToken(ArithmeticParser.OP, 0)

        def EOF(self):
            return self.getToken(ArithmeticParser.EOF, 0)

        def getRuleIndex(self):
            return ArithmeticParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ArithmeticParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(ArithmeticParser.DIGIT)
            self.state = 3
            self.match(ArithmeticParser.OP)
            self.state = 4
            self.match(ArithmeticParser.DIGIT)
            self.state = 5
            self.match(ArithmeticParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





