from unittest import TestCase
from pyottr.stOTTR import stOTTR


TEMPLATE_SIGNATURES = """
    ex:Template1 [ ?a , ?b ] .
    ex:Template2 [ ! owl:Class ?a, ? xsd:int ?b = 5 ] .
    ex:Template3 [ !??a ] .
    """


class StottrShould(TestCase):

    def test_single_minimal_template(self):
        stottr = stOTTR()
        stottr.process("ex:EmptyTemplate [ ] .")
        assert 1 == len(stottr.templates)
        assert None != stottr.templates['ex:EmptyTemplate']

    def test_names_from_templates(self):
        stottr = stOTTR()
        stottr.process(TEMPLATE_SIGNATURES)
        assert 3 == len(stottr.templates)
        assert None != stottr.templates['ex:Template1']
        assert None != stottr.templates['ex:Template2']
        assert None != stottr.templates['ex:Template3']