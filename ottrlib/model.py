from typing import Callable, Iterator, List, Union

from diogi.functions import always_a_list


class Directive:
    pass


class Error:
    def __init__(self, message: str) -> None:
        self.message = message

    def __str__(self):
        return self.message


class LineError(Error):
    def __init__(self, line: int, message: str) -> None:
        super().__init__(message)
        self.line = line

    def __str__(self):
        return f"Line {self.line}: {self.message}"


class Instance:
    def __init__(self, name: str, line: int = None) -> None:
        self.line = line
        self.name = name
        self.arguments = []

    def add_argument(self, argument) -> None:
        if isinstance(argument, Term):
            self.arguments.append(argument)
        else:
            self.arguments.append(Literal(argument))

    def expand_with(self, get_template: Callable[[str], object], variables: dict = {}):
        template = get_template(self.name)
        parameters = Instance._resolve_variables(self.arguments, variables)
        yield from template.expand_with(get_template, *parameters)

    def create_error(self, message: str) -> Error:
        return LineError(self.line, message)

    def __str__(self):
        repr = [str(self.name)]
        repr += ["("]
        repr += [", ".join([str(t) for t in self.arguments])]
        repr += [")"]
        return "".join(repr)

    @staticmethod
    def _resolve_variables(arguments, variables):
        for argument in arguments:
            if isinstance(argument, Variable):
                yield variables[argument.value]
                continue
            yield argument


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
        return f"@prefix {self.label} {self.iri}"

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

    def expand_with(self, get_template: Callable[[str], object], *arguments: tuple):
        variables = {}
        for i in range(len(arguments)):
            variables[self.parameters[i].variable] = arguments[i]

        for i in self.instances:
            yield from i.expand_with(get_template, variables)

    def validate(self, instance: Instance) -> Iterator[Error]:
        def parameters(number: int) -> str:
            if number == 1:
                return "1 parameter"
            else:
                return f"{number} parameters"

        def fewer_parameters(number: int) -> str:
            if number == 0:
                return "none were provided."
            elif number == 1:
                return "only 1 was provided."
            else:
                return f"only {number} were provided."

        def more_parameters(number: int) -> str:
            if number == 0:
                return "none were provided."
            elif number == 1:
                return "1 was provided."
            else:
                return f"{number} were provided."

        if len(instance.arguments) < len(self.parameters):
            yield instance.create_error(
                f"Not enough parameters for an instance of {instance.name}! "
                f"The template expects {parameters(len(self.parameters))} but "
                + fewer_parameters(len(instance.arguments))
            )

        if len(instance.arguments) > len(self.parameters):
            yield instance.create_error(
                f"Too many parameters for an instance of {instance.name}! "
                f"The template expects {parameters(len(self.parameters))} but "
                + more_parameters(len(instance.arguments))
            )

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


class Triple(Template):
    def __init__(self) -> None:
        super().__init__(Iri("ottr:Triple"))

    def expand_with(self, get_template: Callable[[str], object], *parameters) -> str:
        yield " ".join([str(p) for p in parameters])


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
