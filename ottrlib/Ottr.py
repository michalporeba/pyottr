import logging as log
from collections.abc import Iterable
from typing import Callable, Iterator, Union

from .model import Error, Instance, Iri, Template, Triple
from .stOTTRVisitor import stOTTRVisitor


class _Applicator:
    def __init__(
        self, template_name: str, get_template: Callable[[str], Template]
    ) -> None:
        self.template_name = template_name
        self.get_template = get_template

    def to(self, *arguments: tuple) -> Iterator[str]:
        if len(arguments) == 1 and isinstance(arguments[0], Iterable):
            yield from self._to_many(arguments[0])
        else:
            yield from self._to_single(*arguments)

    def _to_single(self, *arguments: tuple) -> Iterator[str]:
        instance = Instance(self.template_name)
        for a in arguments:
            instance.add_argument(a)
        yield from instance.expand_with(self.get_template)

    def _to_many(self, data: Iterator[tuple]) -> Iterator[str]:
        first = True
        for d in data:
            if first:
                first = False
            else:
                yield ""

            yield from self._to_single(*d)


class Ottr:
    TRIPLE_TEMPLATE = Triple()

    def __init__(self):
        self.templates = []

    def get_template(self, name: Union[str, Iri]) -> Union[Template, None]:
        if name == "ottr:Triple":
            return Ottr.TRIPLE_TEMPLATE

        log.debug(f"searching for {name} ({type(name)} in\n{self.templates}")
        results = [t for t in self.templates if t.name == name]
        if len(results) == 0:
            log.warning(f"There is no template {name} defined")
            return None
        return results[0]

    def apply(self, template_name: str):
        return _Applicator(template_name, self.get_template)

    def expand(self, definition: str) -> Iterator[str]:
        first = True

        for element in stOTTRVisitor.get_elements(definition):
            if isinstance(element, Instance):
                if first:
                    first = False
                else:
                    yield ""
                yield from element.expand_with(self.get_template)
                continue
            if isinstance(element, Template):
                self.templates.append(element)
                continue
            log.warning(f"Unknown element type {type(element)} with value {element}")

    def parse(self, definition: str) -> dict:
        instances = 0
        for element in stOTTRVisitor.get_elements(definition):
            if isinstance(element, Instance):
                instances += 1
                continue
            if isinstance(element, Template):
                self.templates.append(element)
                continue
            log.warning(f"Unknown element type {type(element)} with value {element}")
        return {"templates": len(self.templates), "instances": instances}

    def validate(self, definition: str) -> Iterator[Error]:
        for element in stOTTRVisitor.get_elements(definition):
            if isinstance(element, Instance):
                template = self.get_template(element.name)
                if template is None:
                    yield element.create_error(
                        f"An instance of an undefined template {element.name}!"
                    )
                    continue

                yield from template.validate(element)
                continue
