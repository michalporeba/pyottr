from pyottr.PyOTTR import PyOTTR


def test_parse_scenario_01():
    sut = PyOTTR()
    stats = sut.parse(
        """
        ex:Pizza [ ?identifier, ?label ] :: {
            ottr:Triple( ?idnetifier, rdfs:label, ?label )
        } .
        ex:Pizza(p:Margherita, "Margherita") .
        ex:Pizza(p:Hawaii, "Hawaii") .
    """
    )
    assert stats["templates"] == 1
    assert stats["instances"] == 2


def process_scenario_01():
    sut = PyOTTR()
    triples = sut.process(
        """
        ex:Pizza [ ?identifier, ?label ] :: {
            ottr:Triple( ?idnetifier, rdfs:label, ?label )
        } .
        ex:Pizza(p:Margherita, "Margherita") .
        ex:Pizza(p:Hawaii, "Hawaii") .
        ex:Pizza(p:Grandiosa, "Grandiosa") .
    """
    )

    expected = [
        'p:Margherita rdfs:label "Margherita"',
        'p:Hawaii rdfs:label "Hawaii"',
        'p:Grandiosa rdfs:label "Grandiosa"',
    ]

    unexpected = []

    for triple in triples:
        if triple in expected:
            expected.remove(triple)
        else:
            unexpected.append(triple)

    if len(expected) > 0 or len(unexpected) > 0:
        print(f"Missing triples: {expected}")
        print(f"Unexpected triples: {unexpected}")
        raise AssertionError
