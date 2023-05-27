from typing import Iterator, Union

from antlr4 import CommonTokenStream, InputStream

from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import stOTTRParser
from .model import Instance, Iri, Template
from .stOTTRVisitor import stOTTRVisitor


class stOTTR:
    def __init__(self):
        self._templates = []
        self._instances = []

    def get_template(self, name: Union[str, Iri]) -> Union[Template, None]:
        results = [t for t in self._templates if t.name == name]
        if len(results) == 0:   
            return None
        return results[0]

    def parse(self, definition: str) -> dict:
        input_stream = InputStream(definition)
        lexer = stOTTRLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = stOTTRParser(token_stream)
        parse_tree = parser.stOTTRDoc()

        visitor = stOTTRVisitor()
        for element in visitor.visit(parse_tree):
            if isinstance(element, Instance):
                self._instances.append(element)
                continue
            if isinstance(element, Template):
                self._templates.append(element)
                continue
            print(f"Unknown element type {type(element)} with value {element}")
        return {"templates": len(self._templates), "instances": len(self._instances)}

    def process(self, definition: str) -> Iterator[str]:
        return ""
