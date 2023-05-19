from antlr4 import InputStream, CommonTokenStream
from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import stOTTRParser
from .stOTTRVisitor import stOTTRVisitor

class stOTTR:
    def __init__(self):
        self._templates = {}

    def process(self, definition :str) -> None: 
        input_stream = InputStream(definition)
        lexer = stOTTRLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = stOTTRParser(token_stream)
        parse_tree = parser.stOTTRDoc()

        visitor = stOTTRVisitor()
        results = visitor.visit(parse_tree)

        self._templates = self._templates | results['templates']