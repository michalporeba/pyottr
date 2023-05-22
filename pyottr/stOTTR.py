from antlr4 import InputStream, CommonTokenStream
from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import stOTTRParser
from .stOTTRVisitor import stOTTRVisitor
from .model import Template

class stOTTR:
    def __init__(self):
        self._templates = {}

    def get_template(self, iri:str) -> Template:
        results = [t for t in self._templates if t.iri == iri]
        if len(results) == 0:
            return None
        return results[0]


    def parse(self, definition :str) -> None: 
        input_stream = InputStream(definition)
        lexer = stOTTRLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = stOTTRParser(token_stream)
        parse_tree = parser.stOTTRDoc()

        visitor = stOTTRVisitor()
        results = visitor.visit(parse_tree)

        self._templates = self._templates | results['templates']

        return (None, self._templates)