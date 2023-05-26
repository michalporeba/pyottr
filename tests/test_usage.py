from pyottr.stOTTR import stOTTR


def test_parse_scenario_01():
    stottr = stOTTR()
    stats = stottr.parse(
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
