from pyottr.model import Iri
from pyottr.PyOTTR import PyOTTR


def test_parse_scenario_01():
    sut = PyOTTR()
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
    sut = PyOTTR()
    triples = list(
        sut.process(
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
    sut = PyOTTR()
    sut.parse(PIZZA_TEMPLATES)
    triples = list(sut.apply("pz:Pizza").to(Iri("p:Margherita"), "Margherita"))
    expected = [
        "p:Margherita rdf:type owl:Class",
        "p:Margherita rdfs:subClassOf p:Pizza",
        'p:Margherita rdfs:label "Margherita"',
    ]
    assert triples == expected
