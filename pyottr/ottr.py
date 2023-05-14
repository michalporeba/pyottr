from antlr4 import InputStream, CommonTokenStream
from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import stOTTRParser
from .grammar.stOTTRVisitor import stOTTRVisitor

class MyVisitor(stOTTRVisitor):
    def visitStatement(self, ctx):
        print(f"Visited statement: {ctx.getText()}")
        return super().visitStatement(ctx)


def tryit():
    stottr_input = """
    # modifiers
    ex:NamedPizza [ ??pizza  ] .
    ex:NamedPizza [ !?pizza ] .
    ex:NamedPizza [ ?!?pizza ] .
    ex:NamedPizza [ !??pizza ] .
    """
    input_stream = InputStream(stottr_input)
    lexer = stOTTRLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = stOTTRParser(token_stream)
    parse_tree = parser.stOTTRDoc()

    visitor = MyVisitor()
    result = visitor.visit(parse_tree)

    print(result)

