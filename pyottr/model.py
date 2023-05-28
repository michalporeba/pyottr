from typing import List, Union

from diogi.functions import always_a_list


class Directive:
    pass


class Instance:
    def __init__(self, template_name) -> None:
        self._template_name = template_name
        self._arguments = []

    def get_template_name(self):
        return self._template_name

    def add_argument(self, argument) -> None:
        self._arguments.append(argument)

    def expand(self, template, *parameters: tuple) -> str:
        if not self._template_name == "ottr:Triple":
            raise NotImplementedError(
                f"Expanding template {self._template_name} is not implemented"
            )

        if len(self._arguments) != 3:
            raise ValueError("ottr:Triple must have exactly 3 arguments")

        values = template.get_variable_values(parameters)
        triple = []
        for term in self._arguments:
            if isinstance(term, Variable):
                value = values[term.value]
                if isinstance(value, Term):
                    triple.append(str(value))
                else:
                    triple.append(f'"{values[term.value]}"')
                continue
            triple.append(str(term))

        return " ".join(triple)

    def __str__(self):
        repr = [str(self._template_name)]
        repr += ["("]
        repr += [", ".join([str(t) for t in self._arguments])]
        repr += [")"]
        return "".join(repr)


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
    def __init__(self, instances: Union[Instance, List[Instance]]) -> None:
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

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        if isinstance(other, type(self)):
            return self.value == other.value


class Literal(Term):
    def __init__(self, value: Union[str, int, float]) -> None:
        super().__init__(value)

    def __str__(self) -> str:
        if isinstance(self.value, int) or isinstance(self.value, float):
            return str(self.value)
        return f'"{self.value}"'

    def __eq__(self, other) -> bool:
        if isinstance(other, Literal):
            return self.value == other.value
        return self.value == other


class Variable(Term):
    def __init__(self, name: str) -> None:
        super().__init__(name)


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
        for parameter in always_a_list(parameters):
            self.parameters.append(parameter)

    def get_parameter(self, variable: str) -> Parameter:
        return [p for p in self.parameters if p.variable == variable][0]

    def add_instances(self, instances: Union[Instance, List[Instance]]) -> None:
        for instance in always_a_list(instances):
            self.instances.append(instance)

    def get_variable_values(self, values: tuple):
        output = {}
        for i in range(len(values)):
            output[self.parameters[i].variable] = values[i]
        return output

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
