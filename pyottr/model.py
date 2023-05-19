class Template:
    def __init__(self) -> None:
        self.iri = None

    def __str__(self) -> str:
        return f'T(iri:{self.iri})'
    
    def __repr__(self) -> str:
        return self.__str__()
    
class Prefix:
    def __init__(self, namespace:str, iri:str) -> None:
        self.namespace = namespace
        self.iri = iri

    def __str__(self) -> str:
        return f'P({self.namespace} -> {self.iri})'
    
    def __repr__(self) -> str:
        return self.__str__()
