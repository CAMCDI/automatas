# Generated from Calculadora.g4 by ANTLR 4.13.1
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
        4,1,18,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,41,8,3,
        10,3,12,3,44,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,55,8,5,
        10,5,12,5,58,9,5,1,6,1,6,1,6,5,6,63,8,6,10,6,12,6,66,9,6,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,74,8,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,3,1,0,
        10,13,1,0,6,7,1,0,8,9,75,0,19,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,
        6,34,1,0,0,0,8,47,1,0,0,0,10,51,1,0,0,0,12,59,1,0,0,0,14,73,1,0,
        0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,
        1,0,0,0,20,1,1,0,0,0,21,19,1,0,0,0,22,28,3,4,2,0,23,28,3,6,3,0,24,
        25,3,10,5,0,25,26,5,18,0,0,26,28,1,0,0,0,27,22,1,0,0,0,27,23,1,0,
        0,0,27,24,1,0,0,0,28,3,1,0,0,0,29,30,5,2,0,0,30,31,5,5,0,0,31,32,
        3,10,5,0,32,33,5,18,0,0,33,5,1,0,0,0,34,35,5,1,0,0,35,36,5,14,0,
        0,36,37,3,8,4,0,37,38,5,15,0,0,38,42,5,16,0,0,39,41,3,2,1,0,40,39,
        1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,
        44,42,1,0,0,0,45,46,5,17,0,0,46,7,1,0,0,0,47,48,3,10,5,0,48,49,7,
        0,0,0,49,50,3,10,5,0,50,9,1,0,0,0,51,56,3,12,6,0,52,53,7,1,0,0,53,
        55,3,12,6,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,
        0,0,57,11,1,0,0,0,58,56,1,0,0,0,59,64,3,14,7,0,60,61,7,2,0,0,61,
        63,3,14,7,0,62,60,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,
        0,0,65,13,1,0,0,0,66,64,1,0,0,0,67,74,5,3,0,0,68,74,5,2,0,0,69,70,
        5,14,0,0,70,71,3,10,5,0,71,72,5,15,0,0,72,74,1,0,0,0,73,67,1,0,0,
        0,73,68,1,0,0,0,73,69,1,0,0,0,74,15,1,0,0,0,6,19,27,42,56,64,73
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", 
                     "'!='", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "ID", "NUM", "WS", "ASSIGN", 
                      "PLUS", "MINUS", "MULT", "DIV", "GT", "LT", "EQ", 
                      "NEQ", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_condicional = 3
    RULE_condicion = 4
    RULE_expresion = 5
    RULE_termino = 6
    RULE_factor = 7

    ruleNames =  [ "programa", "sentencia", "asignacion", "condicional", 
                   "condicion", "expresion", "termino", "factor" ]

    EOF = Token.EOF
    T__0=1
    ID=2
    NUM=3
    WS=4
    ASSIGN=5
    PLUS=6
    MINUS=7
    MULT=8
    DIV=9
    GT=10
    LT=11
    EQ=12
    NEQ=13
    LPAREN=14
    RPAREN=15
    LBRACE=16
    RBRACE=17
    SEMI=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = CalculadoraParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16398) != 0):
                self.state = 16
                self.sentencia()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(CalculadoraParser.AsignacionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(CalculadoraParser.CondicionalContext,0)


        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def SEMI(self):
            return self.getToken(CalculadoraParser.SEMI, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = CalculadoraParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.asignacion()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.condicional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.expresion()
                self.state = 25
                self.match(CalculadoraParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CalculadoraParser.ASSIGN, 0)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def SEMI(self):
            return self.getToken(CalculadoraParser.SEMI, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = CalculadoraParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(CalculadoraParser.ID)
            self.state = 30
            self.match(CalculadoraParser.ASSIGN)
            self.state = 31
            self.expresion()
            self.state = 32
            self.match(CalculadoraParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(CalculadoraParser.LPAREN, 0)

        def condicion(self):
            return self.getTypedRuleContext(CalculadoraParser.CondicionContext,0)


        def RPAREN(self):
            return self.getToken(CalculadoraParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CalculadoraParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CalculadoraParser.RBRACE, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.SentenciaContext,i)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = CalculadoraParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(CalculadoraParser.T__0)
            self.state = 35
            self.match(CalculadoraParser.LPAREN)
            self.state = 36
            self.condicion()
            self.state = 37
            self.match(CalculadoraParser.RPAREN)
            self.state = 38
            self.match(CalculadoraParser.LBRACE)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16398) != 0):
                self.state = 39
                self.sentencia()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(CalculadoraParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def GT(self):
            return self.getToken(CalculadoraParser.GT, 0)

        def LT(self):
            return self.getToken(CalculadoraParser.LT, 0)

        def EQ(self):
            return self.getToken(CalculadoraParser.EQ, 0)

        def NEQ(self):
            return self.getToken(CalculadoraParser.NEQ, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = CalculadoraParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.expresion()
            self.state = 48
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 49
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.TerminoContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.TerminoContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.PLUS)
            else:
                return self.getToken(CalculadoraParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.MINUS)
            else:
                return self.getToken(CalculadoraParser.MINUS, i)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = CalculadoraParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.termino()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 52
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 53
                self.termino()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.FactorContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.MULT)
            else:
                return self.getToken(CalculadoraParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.DIV)
            else:
                return self.getToken(CalculadoraParser.DIV, i)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = CalculadoraParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.factor()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 60
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 61
                self.factor()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(CalculadoraParser.NUM, 0)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CalculadoraParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(CalculadoraParser.RPAREN, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = CalculadoraParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(CalculadoraParser.NUM)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(CalculadoraParser.ID)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(CalculadoraParser.LPAREN)
                self.state = 70
                self.expresion()
                self.state = 71
                self.match(CalculadoraParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





