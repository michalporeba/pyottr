from typing import List, Union

from diogi.functions import always_a_list


class Directive:
    pass


class Instance:
    def __init__(self, template_name):
        self._template_name = template_name

    def get_template_name(self):
        return self._template_name

    def is_part_of_a_template(self):
        return self._template_name is not None


class Parameter:
    def __init__(self, variable: str) -> None:
        self.variable = variable
        self.default_value = None
        self.optional = False
        self.nonblank = False
        self.type_ = Top()

    def set_default_value(self, default_value: str) -> None:
        self.default_value = default_value

    def set_nonblank(self, nonblank: bool) -> None:
        self.nonblank = nonblank

    def set_optional(self, optional: bool) -> None:
        self.optional = optional

    def __str__(self) -> str:
        repr = []
        if self.optional:
            repr += ["?"]
        if self.nonblank:
            repr += ["!"]
        if self.type_ and not isinstance(self.type_, Top):
            if self.optional or self.nonblank:
                repr += [" "]
            repr += [str(self.type_), " "]
        repr += [self.variable]
        if self.default_value:
            repr += [" = ", f'"{self.default_value}"']
        if len(repr) == 0:
            return ""
        return "".join(repr)


class Patterns:
    def __init__(self, instances):
        self.instances = instances


class Prefix(Directive):
    def __init__(self, label: str, iri: str) -> None:
        self.label = label
        self.iri = iri

    def __str__(self) -> str:
        return f"P({self.label} -> {self.iri})"

    def __repr__(self) -> str:
        return self.__str__()


class Term:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.value == other.value


class Iri(Term):
    def __init__(self, value: str) -> None:
        super().__init__(value)

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.value == other
        return super().__eq__(other)


class Statement:
    pass


class Template(Statement):
    def __init__(self, name: Iri = None) -> None:
        if isinstance(name, str):
            self.name = Iri(name)
        elif isinstance(name, Iri):
            self.name = name
        else:
            raise Exception(
                f"Templates name has to be a str or an Iri! It was {type(name)}"
            )

        self.parameters = []
        self.instances = []

    def add_parameters(self, parameters: Union[Parameter, List[Parameter]]) -> None:
        print(f"parameters = {parameters}")
        if isinstance(parameters, list):
            for parameter in parameters:
                print(f"parameter = {parameter}")
                self.parameters.append(parameter)
        else:
            self.parameters.append(parameters)

    def get_parameter(self, variable: str) -> Parameter:
        return [p for p in self.parameters if p.variable == variable][0]

    def add_instances(self, instances: Union[Instance, List[Instance]]) -> None:
        print(f"pattern instances = {instances}")
        for instance in always_a_list(instances):
            print("pattern instance = {instance}")
            self.instances.append(instance)

    def __str__(self) -> str:
        repr = [str(self.name), " ["]
        if len(self.parameters) > 0:
            repr.append(" ")
            repr.append(", ".join([str(p) for p in self.parameters]))
            repr.append(" ")

        repr += ["] ", "."]
        return "".join(repr)

    def __repr__(self) -> str:
        return self.__str__()


class Type:
    pass


class Top(Type):
    def __eq__(self, other):
        return isinstance(other, Top)


class Basic(Type):
    def __init__(self, iri: str) -> None:
        self.iri = iri

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.iri == other
        if isinstance(other, Basic):
            return self.iri == other.iri
        return NotImplementedError(f"Basic type cannot be compared to {type(other)}!")

    def __str__(self):
        return self.iri


class TypedList(Type):
    def __init__(self, type_: Basic) -> None:
        self.type_ = type_

    def __str__(self):
        return f"List<{self.type_}>"

    def __eq__(self, other):
        if not isinstance(other, TypedList):
            return False
        return self.type_ == other.type_


class LowestUpperBound(Type):
    pass


class NonEmptyList(Type):
    pass
