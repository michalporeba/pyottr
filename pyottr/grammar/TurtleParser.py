# Generated from Turtle.g4 by ANTLR 4.12.0
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
        4,1,35,79,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,0,3,
        0,29,8,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,5,1,5,1,5,3,5,50,8,5,1,6,1,6,1,7,1,7,1,7,1,7,3,7,58,8,
        7,1,8,1,8,3,8,62,8,8,1,9,1,9,1,10,1,10,3,10,68,8,10,1,11,1,11,5,
        11,72,8,11,10,11,12,11,75,9,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,
        12,14,16,18,20,22,0,2,1,0,16,18,1,0,12,13,76,0,28,1,0,0,0,2,30,1,
        0,0,0,4,35,1,0,0,0,6,39,1,0,0,0,8,42,1,0,0,0,10,49,1,0,0,0,12,51,
        1,0,0,0,14,53,1,0,0,0,16,61,1,0,0,0,18,63,1,0,0,0,20,67,1,0,0,0,
        22,69,1,0,0,0,24,29,3,2,1,0,25,29,3,4,2,0,26,29,3,8,4,0,27,29,3,
        6,3,0,28,24,1,0,0,0,28,25,1,0,0,0,28,26,1,0,0,0,28,27,1,0,0,0,29,
        1,1,0,0,0,30,31,5,1,0,0,31,32,5,12,0,0,32,33,5,11,0,0,33,34,5,2,
        0,0,34,3,1,0,0,0,35,36,5,3,0,0,36,37,5,11,0,0,37,38,5,2,0,0,38,5,
        1,0,0,0,39,40,5,4,0,0,40,41,5,11,0,0,41,7,1,0,0,0,42,43,5,5,0,0,
        43,44,5,12,0,0,44,45,5,11,0,0,45,9,1,0,0,0,46,50,3,14,7,0,47,50,
        3,12,6,0,48,50,5,9,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,
        50,11,1,0,0,0,51,52,7,0,0,0,52,13,1,0,0,0,53,57,5,10,0,0,54,58,5,
        15,0,0,55,56,5,6,0,0,56,58,3,16,8,0,57,54,1,0,0,0,57,55,1,0,0,0,
        57,58,1,0,0,0,58,15,1,0,0,0,59,62,5,11,0,0,60,62,3,18,9,0,61,59,
        1,0,0,0,61,60,1,0,0,0,62,17,1,0,0,0,63,64,7,1,0,0,64,19,1,0,0,0,
        65,68,5,14,0,0,66,68,3,22,11,0,67,65,1,0,0,0,67,66,1,0,0,0,68,21,
        1,0,0,0,69,73,5,7,0,0,70,72,5,26,0,0,71,70,1,0,0,0,72,75,1,0,0,0,
        73,71,1,0,0,0,73,74,1,0,0,0,74,76,1,0,0,0,75,73,1,0,0,0,76,77,5,
        8,0,0,77,23,1,0,0,0,6,28,49,57,61,67,73
    ]

class TurtleParser ( Parser ):

    grammarFileName = "Turtle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@prefix'", "'.'", "'@base'", "'BASE'", 
                     "'PREFIX'", "'^^'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "BooleanLiteral", "String", "IRIREF", 
                      "PNAME_NS", "PNAME_LN", "BLANK_NODE_LABEL", "LANGTAG", 
                      "INTEGER", "DECIMAL", "DOUBLE", "EXPONENT", "STRING_LITERAL_QUOTE", 
                      "STRING_LITERAL_SINGLE_QUOTE", "STRING_LITERAL_LONG_SINGLE_QUOTE", 
                      "STRING_LITERAL_LONG_QUOTE", "UCHAR", "ECHAR", "WS", 
                      "PN_CHARS_BASE", "PN_CHARS_U", "PN_CHARS", "PN_PREFIX", 
                      "PN_LOCAL", "PLX", "PERCENT", "HEX", "PN_LOCAL_ESC" ]

    RULE_directive = 0
    RULE_prefixID = 1
    RULE_base = 2
    RULE_sparqlBase = 3
    RULE_sparqlPrefix = 4
    RULE_literal = 5
    RULE_numericLiteral = 6
    RULE_rdfLiteral = 7
    RULE_iri = 8
    RULE_prefixedName = 9
    RULE_blankNode = 10
    RULE_anon = 11

    ruleNames =  [ "directive", "prefixID", "base", "sparqlBase", "sparqlPrefix", 
                   "literal", "numericLiteral", "rdfLiteral", "iri", "prefixedName", 
                   "blankNode", "anon" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    BooleanLiteral=9
    String=10
    IRIREF=11
    PNAME_NS=12
    PNAME_LN=13
    BLANK_NODE_LABEL=14
    LANGTAG=15
    INTEGER=16
    DECIMAL=17
    DOUBLE=18
    EXPONENT=19
    STRING_LITERAL_QUOTE=20
    STRING_LITERAL_SINGLE_QUOTE=21
    STRING_LITERAL_LONG_SINGLE_QUOTE=22
    STRING_LITERAL_LONG_QUOTE=23
    UCHAR=24
    ECHAR=25
    WS=26
    PN_CHARS_BASE=27
    PN_CHARS_U=28
    PN_CHARS=29
    PN_PREFIX=30
    PN_LOCAL=31
    PLX=32
    PERCENT=33
    HEX=34
    PN_LOCAL_ESC=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prefixID(self):
            return self.getTypedRuleContext(TurtleParser.PrefixIDContext,0)


        def base(self):
            return self.getTypedRuleContext(TurtleParser.BaseContext,0)


        def sparqlPrefix(self):
            return self.getTypedRuleContext(TurtleParser.SparqlPrefixContext,0)


        def sparqlBase(self):
            return self.getTypedRuleContext(TurtleParser.SparqlBaseContext,0)


        def getRuleIndex(self):
            return TurtleParser.RULE_directive

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDirective" ):
                return visitor.visitDirective(self)
            else:
                return visitor.visitChildren(self)




    def directive(self):

        localctx = TurtleParser.DirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_directive)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.prefixID()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.base()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.sparqlPrefix()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.sparqlBase()
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


    class PrefixIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PNAME_NS(self):
            return self.getToken(TurtleParser.PNAME_NS, 0)

        def IRIREF(self):
            return self.getToken(TurtleParser.IRIREF, 0)

        def getRuleIndex(self):
            return TurtleParser.RULE_prefixID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixID" ):
                return visitor.visitPrefixID(self)
            else:
                return visitor.visitChildren(self)




    def prefixID(self):

        localctx = TurtleParser.PrefixIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prefixID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(TurtleParser.T__0)
            self.state = 31
            self.match(TurtleParser.PNAME_NS)
            self.state = 32
            self.match(TurtleParser.IRIREF)
            self.state = 33
            self.match(TurtleParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IRIREF(self):
            return self.getToken(TurtleParser.IRIREF, 0)

        def getRuleIndex(self):
            return TurtleParser.RULE_base

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase" ):
                return visitor.visitBase(self)
            else:
                return visitor.visitChildren(self)




    def base(self):

        localctx = TurtleParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(TurtleParser.T__2)
            self.state = 36
            self.match(TurtleParser.IRIREF)
            self.state = 37
            self.match(TurtleParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SparqlBaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IRIREF(self):
            return self.getToken(TurtleParser.IRIREF, 0)

        def getRuleIndex(self):
            return TurtleParser.RULE_sparqlBase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSparqlBase" ):
                return visitor.visitSparqlBase(self)
            else:
                return visitor.visitChildren(self)




    def sparqlBase(self):

        localctx = TurtleParser.SparqlBaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sparqlBase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(TurtleParser.T__3)
            self.state = 40
            self.match(TurtleParser.IRIREF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SparqlPrefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PNAME_NS(self):
            return self.getToken(TurtleParser.PNAME_NS, 0)

        def IRIREF(self):
            return self.getToken(TurtleParser.IRIREF, 0)

        def getRuleIndex(self):
            return TurtleParser.RULE_sparqlPrefix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSparqlPrefix" ):
                return visitor.visitSparqlPrefix(self)
            else:
                return visitor.visitChildren(self)




    def sparqlPrefix(self):

        localctx = TurtleParser.SparqlPrefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sparqlPrefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(TurtleParser.T__4)
            self.state = 43
            self.match(TurtleParser.PNAME_NS)
            self.state = 44
            self.match(TurtleParser.IRIREF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rdfLiteral(self):
            return self.getTypedRuleContext(TurtleParser.RdfLiteralContext,0)


        def numericLiteral(self):
            return self.getTypedRuleContext(TurtleParser.NumericLiteralContext,0)


        def BooleanLiteral(self):
            return self.getToken(TurtleParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return TurtleParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = TurtleParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.rdfLiteral()
                pass
            elif token in [16, 17, 18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.numericLiteral()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.match(TurtleParser.BooleanLiteral)
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


    class NumericLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(TurtleParser.INTEGER, 0)

        def DECIMAL(self):
            return self.getToken(TurtleParser.DECIMAL, 0)

        def DOUBLE(self):
            return self.getToken(TurtleParser.DOUBLE, 0)

        def getRuleIndex(self):
            return TurtleParser.RULE_numericLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumericLiteral" ):
                return visitor.visitNumericLiteral(self)
            else:
                return visitor.visitChildren(self)




    def numericLiteral(self):

        localctx = TurtleParser.NumericLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numericLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RdfLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def String(self):
            return self.getToken(TurtleParser.String, 0)

        def LANGTAG(self):
            return self.getToken(TurtleParser.LANGTAG, 0)

        def iri(self):
            return self.getTypedRuleContext(TurtleParser.IriContext,0)


        def getRuleIndex(self):
            return TurtleParser.RULE_rdfLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRdfLiteral" ):
                return visitor.visitRdfLiteral(self)
            else:
                return visitor.visitChildren(self)




    def rdfLiteral(self):

        localctx = TurtleParser.RdfLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rdfLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(TurtleParser.String)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 54
                self.match(TurtleParser.LANGTAG)
                pass
            elif token in [6]:
                self.state = 55
                self.match(TurtleParser.T__5)
                self.state = 56
                self.iri()
                pass
            elif token in [-1]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IriContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IRIREF(self):
            return self.getToken(TurtleParser.IRIREF, 0)

        def prefixedName(self):
            return self.getTypedRuleContext(TurtleParser.PrefixedNameContext,0)


        def getRuleIndex(self):
            return TurtleParser.RULE_iri

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIri" ):
                return visitor.visitIri(self)
            else:
                return visitor.visitChildren(self)




    def iri(self):

        localctx = TurtleParser.IriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_iri)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(TurtleParser.IRIREF)
                pass
            elif token in [12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.prefixedName()
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


    class PrefixedNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PNAME_LN(self):
            return self.getToken(TurtleParser.PNAME_LN, 0)

        def PNAME_NS(self):
            return self.getToken(TurtleParser.PNAME_NS, 0)

        def getRuleIndex(self):
            return TurtleParser.RULE_prefixedName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefixedName" ):
                return visitor.visitPrefixedName(self)
            else:
                return visitor.visitChildren(self)




    def prefixedName(self):

        localctx = TurtleParser.PrefixedNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_prefixedName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlankNodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLANK_NODE_LABEL(self):
            return self.getToken(TurtleParser.BLANK_NODE_LABEL, 0)

        def anon(self):
            return self.getTypedRuleContext(TurtleParser.AnonContext,0)


        def getRuleIndex(self):
            return TurtleParser.RULE_blankNode

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlankNode" ):
                return visitor.visitBlankNode(self)
            else:
                return visitor.visitChildren(self)




    def blankNode(self):

        localctx = TurtleParser.BlankNodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_blankNode)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(TurtleParser.BLANK_NODE_LABEL)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.anon()
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


    class AnonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(TurtleParser.WS)
            else:
                return self.getToken(TurtleParser.WS, i)

        def getRuleIndex(self):
            return TurtleParser.RULE_anon

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnon" ):
                return visitor.visitAnon(self)
            else:
                return visitor.visitChildren(self)




    def anon(self):

        localctx = TurtleParser.AnonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_anon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(TurtleParser.T__6)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 70
                self.match(TurtleParser.WS)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(TurtleParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





