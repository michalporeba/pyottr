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
        self.templates = []

    def get_template(self, name: Union[str, Iri]) -> Union[Template, None]:
        if name == "ottr:Triple":
            return PyOTTR.TRIPLE_TEMPLATE

        results = [t for t in self.templates if t.name == name]
        if len(results) == 0:
            log.warning(f"There is no template {name} defined")
            return None
        return results[0]

    def parse(self, definition: str) -> dict:
        instances = 0
        for element in PyOTTR._visit_definition(definition):
            if isinstance(element, Instance):
                instances += 1
                continue
            if isinstance(element, Template):
                self.templates.append(element)
                continue
            log.warning(f"Unknown element type {type(element)} with value {element}")
        return {"templates": len(self.templates), "instances": instances}

    def process(self, definition: str) -> Iterator[str]:
        first = True

        def get_template(name: str) -> Template:
            return self.get_template(name)

        for element in PyOTTR._visit_definition(definition):
            if isinstance(element, Instance):
                if first:
                    first = False
                else:
                    yield ""
                yield from element.expand_with(get_template)
                continue
            if isinstance(element, Template):
                self.templates.append(element)
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
