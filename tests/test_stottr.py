from unittest import TestCase
from pyottr.stOTTR import stOTTR

class StottrShould(TestCase):

    def test_empty_definition_has_no_effect(self):
        stottr = stOTTR()
        stottr.process("")
        assert 0 == len(stottr.templates)
        