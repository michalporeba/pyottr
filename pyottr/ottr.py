from pyottr.PyOTTR import PyOTTR


def tryit():
    stottr_input = """
    ax:SubClassOf [ ?sub, ?super ] :: {
        ottr:Triple(?sub, rdfs:subClassOf, ?super)
    } .

    pz:Pizza [ ?identifier, ?label ] :: {
        ottr:Triple(?identifier, rdf:type, owl:Class),
        ax:SubClassOf(?identifier, p:Pizza),
        ottr:Triple(?identifier, rdfs:label, ?label)
    } .

    pz:Pizza(p:Margherita, "Margherita") .
    pz:Pizza(p:Hawaii, "Hawaii") .
    pz:Pizza(p:Grandiosa, "Grandiosa") .
    """

    pyottr = PyOTTR()
    for triple in pyottr.process(stottr_input):
        print(triple)

    print()
    for triple in pyottr.process('pz:Pizza(p:Pepperoni, "Pepperoni") .'):
        print(triple)
