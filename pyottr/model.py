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
        return ''.join(repr)


class Prefix:
    def __init__(self, namespace:str, iri:str) -> None:
        self.namespace = namespace
        self.iri = iri

    def __str__(self) -> str:
        return f'P({self.namespace} -> {self.iri})'
    
    def __repr__(self) -> str:
        return self.__str__()


class Template:
    def __init__(self) -> None:
        self.iri = None
        self.parameters = []

    def __str__(self) -> str:
        return f'T(iri:{self.iri})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
