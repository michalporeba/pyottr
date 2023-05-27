import logging as log
from typing import Iterator, Union

from antlr4 import CommonTokenStream, InputStream

from .grammar.stOTTRLexer import stOTTRLexer
from .grammar.stOTTRParser import ParserRuleContext, stOTTRParser
from .model import Instance, Iri, Template
from .stOTTRVisitor import stOTTRVisitor


class PyOTTR:
    def __init__(self):
        self._templates = []
        self._instances = []

    def get_template(self, name: Union[str, Iri]) -> Union[Template, None]:
        results = [t for t in self._templates if t.name == name]
        if len(results) == 0:
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
        for element in PyOTTR._visit_definition(definition):
            if isinstance(element, Instance):
                template = self.get_template(element.get_template_name())
                if template is None:
                    log.warning(
                        f"There is no template {element.get_template_name()} defined"
                    )
                    continue

                self._instances.append(element)
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
