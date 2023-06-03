from ottrlib.model import Iri
from ottrlib.Ottr import Ottr


def test_parse_scenario_01():
    sut = Ottr()
    stats = sut.parse(
        """
        ex:Pizza [ ?identifier, ?label ] :: {
            ottr:Triple( ?identifier, rdfs:label, ?label )
        } .
        ex:Pizza(p:Margherita, "Margherita") .
        ex:Pizza(p:Hawaii, "Hawaii") .
    """
    )
    assert stats["templates"] == 1
    assert stats["instances"] == 2


def test_process_scenario_01():
    sut = Ottr()
    triples = list(
        sut.expand(
            """
        ex:Pizza [ ?identifier, ?label ] :: {
            ottr:Triple( ?identifier, rdfs:label, ?label )
        } .
        ex:Pizza(p:Margherita, "Margherita") .
        ex:Pizza(p:Hawaii, "Hawaii") .
        ex:Pizza(p:Grandiosa, "Grandiosa") .
    """
        )
    )

    expected = [
        'p:Margherita rdfs:label "Margherita"',
        "",
        'p:Hawaii rdfs:label "Hawaii"',
        "",
        'p:Grandiosa rdfs:label "Grandiosa"',
    ]

    assert triples == expected


PIZZA_TEMPLATES = """
    ax:SubClassOf [ ?sub, ?super ] :: {
        ottr:Triple(?sub, rdfs:subClassOf, ?super)
    } .

    pz:Pizza [ ?identifier, ?label ] :: {
        ottr:Triple(?identifier, rdf:type, owl:Class),
        ax:SubClassOf(?identifier, p:Pizza),
        ottr:Triple(?identifier, rdfs:label, ?label)
    } .
    """


def test_processing_pizzas_from_data_in_arguments():
    sut = Ottr()
    sut.parse(PIZZA_TEMPLATES)
    triples = list(sut.apply("pz:Pizza").to(Iri("p:Margherita"), "Margherita"))
    expected = [
        "p:Margherita rdf:type owl:Class",
        "p:Margherita rdfs:subClassOf p:Pizza",
        'p:Margherita rdfs:label "Margherita"',
    ]
    assert triples == expected


def test_processing_pizzas_from_data_in_array():
    sut = Ottr()
    sut.parse(PIZZA_TEMPLATES)
    data = [(Iri("p:Margherita"), "Margherita"), (Iri("p:Hawaii"), "Hawaii")]
    triples = list(sut.apply("pz:Pizza").to(data))
    expected = [
        "p:Margherita rdf:type owl:Class",
        "p:Margherita rdfs:subClassOf p:Pizza",
        'p:Margherita rdfs:label "Margherita"',
        "",
        "p:Hawaii rdf:type owl:Class",
        "p:Hawaii rdfs:subClassOf p:Pizza",
        'p:Hawaii rdfs:label "Hawaii"',
    ]
    assert triples == expected


def test_processing_pizzas_from_data_generator():
    sut = Ottr()
    sut.parse(PIZZA_TEMPLATES)

    def data_generator():
        yield Iri("p:Margherita"), "Margherita"
        yield Iri("p:Hawaii"), "Hawaii"

    triples = list(sut.apply("pz:Pizza").to(data_generator()))
    expected = [
        "p:Margherita rdf:type owl:Class",
        "p:Margherita rdfs:subClassOf p:Pizza",
        'p:Margherita rdfs:label "Margherita"',
        "",
        "p:Hawaii rdf:type owl:Class",
        "p:Hawaii rdfs:subClassOf p:Pizza",
        'p:Hawaii rdfs:label "Hawaii"',
    ]
    assert triples == expected


def test_deeper_nesting():
    sut = Ottr()
    rdf = list(
        sut.expand(
            """
    ex:A[?x] :: {
        ottr:Triple(p:Test, rdfs:label, ?x),
        ottr:Triple(p:Test, rdfs:label, "A")
    } .
    ex:B[?x] :: { ex:A(?x) } .
    ex:C[?x] :: { ex:B(?x), ottr:Triple(p:Test, rdfs:label, "C") } .
    ex:D[?x] :: { ex:C(?x) } .

    ex:D("Test Argument") .
    """
        )
    )

    expected = [
        'p:Test rdfs:label "Test Argument"',
        'p:Test rdfs:label "A"',
        'p:Test rdfs:label "C"',
    ]

    assert rdf == expected


def test_validation_for_missing_template():
    sut = Ottr()
    sut.parse("ex:X[?x] :: { ex:A(?x) } .")
    errors = list(
        sut.validate(
            """
        ex:B("test") .
        """
        )
    )

    expected = ["Line 2: An instance of an undefined template ex:B!"]

    assert [str(e) for e in errors] == expected


def test_validation_for_incorrect_number_of_parameters():
    sut = Ottr()
    sut.parse(
        """
    ex:T[?a, ?b] :: { ottr:Triple(?a, rdfs:label, ?b) } .
    ex:X[?x] :: { ottr:Triple(?x, rdfs:label, "test") } .
    """
    )
    errors = list(
        sut.validate(
            """
    ex:T(p:Test, "test") .
    ex:T(p:Test) .
    ex:T() .
    ex:X() .
    ex:X(p:Test) .
    ex:X(p:Test, "test") .
    """
        )
    )

    expected = [
        "Line 3: Not enough parameters for an instance of ex:T! "
        "The template expects 2 parameters but only 1 was provided.",
        "Line 4: Not enough parameters for an instance of ex:T! "
        "The template expects 2 parameters but none were provided.",
        "Line 5: Not enough parameters for an instance of ex:X! "
        "The template expects 1 parameter but none were provided.",
        "Line 7: Too many parameters for an instance of ex:X! "
        "The template expects 1 parameter but 2 were provided.",
    ]

    assert [str(e) for e in errors] == expected
