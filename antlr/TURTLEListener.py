# Generated from Turtle.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TurtleParser import TurtleParser
else:
    from TurtleParser import TurtleParser

# This class defines a complete listener for a parse tree produced by TurtleParser.
class TurtleListener(ParseTreeListener):

    # Enter a parse tree produced by TurtleParser#directive.
    def enterDirective(self, ctx:TurtleParser.DirectiveContext):
        pass

    # Exit a parse tree produced by TurtleParser#directive.
    def exitDirective(self, ctx:TurtleParser.DirectiveContext):
        pass


    # Enter a parse tree produced by TurtleParser#prefixID.
    def enterPrefixID(self, ctx:TurtleParser.PrefixIDContext):
        pass

    # Exit a parse tree produced by TurtleParser#prefixID.
    def exitPrefixID(self, ctx:TurtleParser.PrefixIDContext):
        pass


    # Enter a parse tree produced by TurtleParser#base.
    def enterBase(self, ctx:TurtleParser.BaseContext):
        pass

    # Exit a parse tree produced by TurtleParser#base.
    def exitBase(self, ctx:TurtleParser.BaseContext):
        pass


    # Enter a parse tree produced by TurtleParser#sparqlBase.
    def enterSparqlBase(self, ctx:TurtleParser.SparqlBaseContext):
        pass

    # Exit a parse tree produced by TurtleParser#sparqlBase.
    def exitSparqlBase(self, ctx:TurtleParser.SparqlBaseContext):
        pass


    # Enter a parse tree produced by TurtleParser#sparqlPrefix.
    def enterSparqlPrefix(self, ctx:TurtleParser.SparqlPrefixContext):
        pass

    # Exit a parse tree produced by TurtleParser#sparqlPrefix.
    def exitSparqlPrefix(self, ctx:TurtleParser.SparqlPrefixContext):
        pass


    # Enter a parse tree produced by TurtleParser#literal.
    def enterLiteral(self, ctx:TurtleParser.LiteralContext):
        pass

    # Exit a parse tree produced by TurtleParser#literal.
    def exitLiteral(self, ctx:TurtleParser.LiteralContext):
        pass


    # Enter a parse tree produced by TurtleParser#numericLiteral.
    def enterNumericLiteral(self, ctx:TurtleParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by TurtleParser#numericLiteral.
    def exitNumericLiteral(self, ctx:TurtleParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by TurtleParser#rdfLiteral.
    def enterRdfLiteral(self, ctx:TurtleParser.RdfLiteralContext):
        pass

    # Exit a parse tree produced by TurtleParser#rdfLiteral.
    def exitRdfLiteral(self, ctx:TurtleParser.RdfLiteralContext):
        pass


    # Enter a parse tree produced by TurtleParser#iri.
    def enterIri(self, ctx:TurtleParser.IriContext):
        pass

    # Exit a parse tree produced by TurtleParser#iri.
    def exitIri(self, ctx:TurtleParser.IriContext):
        pass


    # Enter a parse tree produced by TurtleParser#prefixedName.
    def enterPrefixedName(self, ctx:TurtleParser.PrefixedNameContext):
        pass

    # Exit a parse tree produced by TurtleParser#prefixedName.
    def exitPrefixedName(self, ctx:TurtleParser.PrefixedNameContext):
        pass


    # Enter a parse tree produced by TurtleParser#blankNode.
    def enterBlankNode(self, ctx:TurtleParser.BlankNodeContext):
        pass

    # Exit a parse tree produced by TurtleParser#blankNode.
    def exitBlankNode(self, ctx:TurtleParser.BlankNodeContext):
        pass


    # Enter a parse tree produced by TurtleParser#anon.
    def enterAnon(self, ctx:TurtleParser.AnonContext):
        pass

    # Exit a parse tree produced by TurtleParser#anon.
    def exitAnon(self, ctx:TurtleParser.AnonContext):
        pass



del TurtleParser