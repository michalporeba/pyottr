from antlr4 import InputStream, CommonTokenStream
from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import stOTTRParser
from .grammar.stOTTRVisitor import stOTTRVisitor
from .grammar.TurtleLexer import TurtleLexer
from .grammar.TurtleParser import TurtleParser
from .grammar.TurtleVisitor import TurtleVisitor


class MyStottrVisitor(stOTTRVisitor):
    def visitStatement(self, ctx):
        print(f"Visited statement: {ctx.getText()}")
        return super().visitStatement(ctx)

    # Visit a parse tree produced by stOTTRParser#signature.
    def visitSignature(self, ctx:stOTTRParser.SignatureContext):
        print(f"Visited signature: {ctx.getText()}")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stOTTRParser#templateName.
    def visitTemplateName(self, ctx:stOTTRParser.TemplateNameContext):
        print(f"Visited template name: {ctx.getText()}")
        return self.visitChildren(ctx)

class MyTurtleVisitor(TurtleVisitor):

    # Visit a parse tree produced by TurtleParser#directive.
    def visitDirective(self, ctx:TurtleParser.DirectiveContext):
        print(f"Visited directive: {ctx.getText()}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TurtleParser#prefixID.
    def visitPrefixID(self, ctx:TurtleParser.PrefixIDContext):
        print(f"Visited prefix ID: {ctx.getText()}")
        return self.visitChildren(ctx)



def tryit():
    stottr_input = """
    @prefix : <http://example.xyz/ns> .
    @prefix ex: <http://example.net/ns> .
    PREFIX ex2: <http://example.com/ns>

    # modifiers
    ex:NamedPizzaA [ ??pizza  ] .
    ex:NamedPizzaB [ !?pizza ] .
    ex:NamedPizzaC [ ?!?pizza ] .
    ex:NamedPizzaD [ !??pizza ] .
    """
    input_stream = InputStream(stottr_input)
    lexer = stOTTRLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = stOTTRParser(token_stream)
    parse_tree = parser.stOTTRDoc()

    ttl_stream = InputStream(stottr_input)
    ttl_lexer = TurtleLexer(ttl_stream)
    ttl_token_stream = CommonTokenStream(ttl_lexer)
    ttl_parser = TurtleParser(ttl_token_stream)
    ttl_parse_tree = ttl_parser.turtleDoc()

    ttl_visitor = MyTurtleVisitor()
    ttl_visitor.visit(ttl_parse_tree)

    visitor = MyStottrVisitor()
    result = visitor.visit(parse_tree)

    print(result)

