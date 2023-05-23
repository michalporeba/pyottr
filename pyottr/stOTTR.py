from antlr4 import CommonTokenStream, InputStream

from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import stOTTRParser
from .model import Iri, Template
from .stOTTRVisitor import stOTTRVisitor


class stOTTR:
    def __init__(self):
        self._templates = []

    def get_template(self, name:str|Iri) -> Template:
        results = [t for t in self._templates if t.name == name]
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
        (_, templates) = visitor.visit(parse_tree)

        self._templates += templates

        return (None, self._templates)