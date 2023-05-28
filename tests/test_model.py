from pyottr.model import (
    Instance,
    Iri,
    Literal,
    Parameter,
    Prefix,
    Template,
    Term,
    Triple,
    Variable,
)


def test_simple_parameter_name():
    assert str(Parameter("?a")) == "?a"
    assert str(Parameter("?b")) == "?b"


def test_optional_parameter():
    sut = Parameter("?name")
    assert str(sut) == "?name"
    sut.set_optional(True)
    assert str(sut) == "??name"


def test_nonempty_parameter():
    sut = Parameter("?x")
    assert str(sut) == "?x"
    sut.set_nonblank(True)
    assert str(sut) == "!?x"


def test_optional_nonempty_parameter():
    sut = Parameter("?hello")
    sut.set_nonblank(True)
    sut.set_optional(True)
    assert str(sut) == "?!?hello"


def test_default_value_parameter():
    sut = Parameter("?withDefault")
    sut.set_default_value("xyz")
    assert str(sut) == '?withDefault = "xyz"'


def test_prefix_instantiation():
    sut = Prefix("l:", "hello")
    assert sut.label == "l:"
    assert sut.iri == "hello"


def test_template_with_no_parameters():
    sut = Template("ex:example")
    assert isinstance(sut.name, Iri)
    assert sut.name == "ex:example"
    assert len(sut.parameters) == 0
    assert str(sut) == "ex:example [] ."


def test_template_with_single_parameter():
    sut = Template("ex:test")
    sut.add_parameters(Parameter("?pizza"))
    assert isinstance(sut.name, Iri)
    assert sut.name == "ex:test"
    assert len(sut.parameters) == 1
    assert str(sut) == "ex:test [ ?pizza ] ."


def test_term_equality():
    assert Term(1) == Term(1)
    assert Term("a") == Term("a")
    assert Iri("ex:Pizza") == Iri("ex:Pizza")


def test_term_inequality():
    assert Term(1) != Term(2)
    assert Term("a") != Term("b")
    assert Term("abc") != Term(123)
    assert Iri(":Pizza") != Iri("ex:Pizza")


def test_expand_triple_template():
    triple = Triple()
    assert list(
        triple.expand_with(None, Iri("p:Hawaii"), Term("rdf:type"), Term("owl:Class"))
    ) == ["p:Hawaii rdf:type owl:Class"]


def test_expand_triple_instance():
    instance = Instance(Iri("ottr:Triple"))
    instance.add_argument(Iri("p:Grandiosa"))
    instance.add_argument(Term("rdf:type"))
    instance.add_argument(Term("owl:Class"))

    def get_template(name: str):
        if name == "ottr:Triple":
            return Triple()
        raise AssertionError(f"Incorrect template {name} has been requested!")

    assert list(instance.expand_with(get_template)) == [
        "p:Grandiosa rdf:type owl:Class"
    ]


def test_expand_triple_instance_with_variable_substitution():
    instance = Instance(Iri("ottr:Triple"))
    instance.add_argument(Variable("?identifier"))
    instance.add_argument(Term("rdfs:label"))
    instance.add_argument(Variable("?label"))

    def get_template(name: str):
        if name == "ottr:Triple":
            return Triple()
        raise AssertionError(f"Incorrect template {name} has been requested!")

    variables = {"?identifier": Iri("p:Margherita"), "?label": Literal("Margherita")}
    assert list(instance.expand_with(get_template, variables)) == [
        'p:Margherita rdfs:label "Margherita"'
    ]


def test_expand_top_level_instance():
    pizza = Template(Iri("ex:Pizza"))
    pizza.add_parameters(Parameter("?identifier"))
    pizza.add_parameters(Parameter("?label"))

    pattern_type = Instance("ottr:Triple")
    pattern_type.add_argument(Variable("?identifier"))
    pattern_type.add_argument(Iri("rdf:type"))
    pattern_type.add_argument(Iri("owl:Class"))
    pizza.add_instances(pattern_type)

    pattern_label = Instance("ottr:Triple")
    pattern_label.add_argument(Variable("?identifier"))
    pattern_label.add_argument(Iri("rdfs:label"))
    pattern_label.add_argument(Variable("?label"))
    pizza.add_instances(pattern_label)

    def get_template(name: str):
        if name == "ottr:Triple":
            return Triple()
        if name == "ex:Pizza":
            return pizza
        raise AssertionError(f"Incorrect template {name} has been requested!")

    instance = Instance("ex:Pizza")
    instance.add_argument(Iri("p:Grandiosa"))
    instance.add_argument(Literal("Grandiosa"))

    assert list(instance.expand_with(get_template)) == [
        "p:Grandiosa rdf:type owl:Class",
        'p:Grandiosa rdfs:label "Grandiosa"',
    ]


def test_expand_top_level_instance_with_recursion():
    subclass = Template(Iri("ax:SubClassOf"))
    subclass.add_parameters(Parameter("?sub"))
    subclass.add_parameters(Parameter("?super"))

    pattern = Instance("ottr:Triple")
    pattern.add_argument(Variable("?sub"))
    pattern.add_argument(Iri("rdfs:subClassOf"))
    pattern.add_argument(Variable("?super"))
    subclass.add_instances(pattern)

    pizza = Template(Iri("ex:Pizza"))
    pizza.add_parameters(Parameter("?identifier"))
    pizza.add_parameters(Parameter("?label"))

    pattern_type = Instance("ottr:Triple")
    pattern_type.add_argument(Variable("?identifier"))
    pattern_type.add_argument(Iri("rdf:type"))
    pattern_type.add_argument(Iri("owl:Class"))
    pizza.add_instances(pattern_type)

    pattern_sub = Instance("ax:SubClassOf")
    pattern_sub.add_argument(Variable("?identifier"))
    pattern_sub.add_argument(Iri("p:Pizza"))
    pizza.add_instances(pattern_sub)

    pattern_label = Instance("ottr:Triple")
    pattern_label.add_argument(Variable("?identifier"))
    pattern_label.add_argument(Iri("rdfs:label"))
    pattern_label.add_argument(Variable("?label"))
    pizza.add_instances(pattern_label)

    def get_template(name: str):
        if name == "ottr:Triple":
            return Triple()
        if name == "ex:Pizza":
            return pizza
        if name == "ax:SubClassOf":
            return subclass
        raise AssertionError(f"Incorrect template {name} has been requested!")

    instance = Instance("ex:Pizza")
    instance.add_argument(Iri("p:Hawaii"))
    instance.add_argument(Literal("Hawaii"))

    assert list(instance.expand_with(get_template)) == [
        "p:Hawaii rdf:type owl:Class",
        "p:Hawaii rdfs:subClassOf p:Pizza",
        'p:Hawaii rdfs:label "Hawaii"',
    ]
