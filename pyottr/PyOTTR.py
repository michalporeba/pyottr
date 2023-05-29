import logging as log
from typing import Iterator, Union

from antlr4 import CommonTokenStream, InputStream

from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import ParserRuleContext, stOTTRParser
from .model import Instance, Iri, Template, Triple
from .stOTTRVisitor import stOTTRVisitor


class PyOTTR:
    TRIPLE_TEMPLATE = Triple()

    def __init__(self):
        self._templates = []
        self._instances = []

    def get_template(self, name: Union[str, Iri]) -> Union[Template, None]:
        if name == "ottr:Triple":
            return PyOTTR.TRIPLE_TEMPLATE

        results = [t for t in self._templates if t.name == name]
        if len(results) == 0:
            log.warning(f"There is no template {name} defined")
            return None
        return results[0]

    def parse(self, definition: str) -> dict:
        for element in PyOTTR._visit_definition(definition):
            if isinstance(element, Instance):
                self._instances.append(element)
                continue
            if isinstance(element, Template):
                self._templates.append(element)
                continue
            log.warning(f"Unknown element type {type(element)} with value {element}")
        return {"templates": len(self._templates), "instances": len(self._instances)}

    def process(self, definition: str) -> Iterator[str]:
        def get_template(name: str) -> Template:
            print(f"Getting template: {name}")
            template = self.get_template(name)
            print(f"Template is {template}")
            return template

        for element in PyOTTR._visit_definition(definition):
            if isinstance(element, Instance):
                yield from element.expand_with(get_template)
                continue
            if isinstance(element, Template):
                self._templates.append(element)
                continue
            log.warning(f"Unknown element type {type(element)} with value {element}")

    @staticmethod
    def _visit_definition(definition: str):
        parse_tree = PyOTTR._create_parse_tree(definition)
        visitor = stOTTRVisitor()
        return visitor.visit(parse_tree)

    @staticmethod
    def _create_parse_tree(definition: str) -> ParserRuleContext:
        input_stream = InputStream(definition)
        lexer = stOTTRLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = stOTTRParser(token_stream)
        return parser.stOTTRDoc()
