from antlr4 import InputStream, CommonTokenStream
from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import stOTTRParser
from .stOTTRVisitor import stOTTRVisitor

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

    visitor = stOTTRVisitor()
    result = visitor.visit(parse_tree)

    print(result)

