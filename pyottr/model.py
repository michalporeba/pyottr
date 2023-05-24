from typing import List, Union

class Directive:
    pass


class Parameter:
    def __init__(self, variable: str) -> None:
        self.variable = variable
        self.default_value = None
        self.optional = False
        self.nonblank = False
        self.type_ = None

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
        if self.type_:
            if self.optional or self.nonblank:
                repr += [" "]
            repr += [str(self.type_), " "]
        repr += [self.variable]
        if self.default_value:
            repr += [" = ", f'"{self.default_value}"']
        if len(repr) == 0:
            return ""
        return "".join(repr)


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


class Basic(Type):
    def __init__(self, iri: str) -> None:
        self.iri = iri

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.iri == other
        return super().__eq__(other)

    def __str__(self):
        return self.iri


class List(Type):
    pass


class LowestUpperBound(Type):
    pass


class NonEmptyList(Type):
    pass
