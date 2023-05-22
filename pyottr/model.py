class Directive:
    pass

class Parameter:
    def __init__(self, variable):
        self.variable = variable
        self.default_value = None
        self.optional = False 
        self.nonblank = False

    def set_default_value(self, default_value:str) -> None: 
        self.default_value = default_value

    def set_nonblank(self, nonblank:bool) -> None:
        self.nonblank = nonblank

    def set_optional(self, optional:bool) -> None:
        self.optional = optional
    
    def __str__(self) -> str:
        repr = []
        if self.optional:
            repr += ['?']
        if self.nonblank:
            repr += ['!']
        repr += [self.variable]
        if self.default_value:
            repr += [' = ', f'"{self.default_value}"']
        if len(repr) == 0:
            return ''
        return ''.join(repr)
        

class Prefix(Directive):
    def __init__(self, label:str, iri:str) -> None:
        self.label = label
        self.iri = iri

    def __str__(self) -> str:
        return f'P({self.label} -> {self.iri})'
    
    def __repr__(self) -> str:
        return self.__str__()


class Statement:
    pass


class Template(Statement):
    def __init__(self, iri:str=None) -> None:
        self.iri = iri
        self.parameters = []

    def add_parameter(self, parameter:Parameter) -> None:
        print(f' type(parameter) == {type(parameter)}')
        self.parameters.append(parameter)

    def get_parameter(self, variable:str) -> Parameter:
        return [p for p in self.parameters if p.variable == variable][0]

    def __str__(self) -> str:
        repr = [self.iri, ' [']
        if len(self.parameters) > 0:
            repr.append(' ')
            repr.append(', '.join([str(p) for p in self.parameters]))
            repr.append(' ')

        repr += ['] ', '.']
        return ''.join(repr)
    
    def __repr__(self) -> str:
        return self.__str__()
    

class Term:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.value == other.value


class Iri(Term):
    def __init__(self, value):
        super().__init__(value)

