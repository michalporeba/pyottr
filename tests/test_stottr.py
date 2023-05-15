from unittest import TestCase
from pyottr.stOTTR import stOTTR

class StottrShould(TestCase):

    def test_single_minimal_template(self):
        stottr = stOTTR()
        stottr.process("ex:EmptyTemplate [ ] .")
        assert 1 == len(stottr.templates)
        assert None != stottr.templates['ex:EmptyTemplate']