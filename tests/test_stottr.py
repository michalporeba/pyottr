from unittest import TestCase
from pyottr.stOTTR import stOTTR


TEMPLATE_SIGNATURES = """
ex:Template1 [ ?a , ?b ] .
ex:Template2 [ ! owl:Class ?a, ? xsd:int ?b = 5 ] .
ex:Template3 [ !??a ] .
"""

TEMPLATES = """
# This is a base template:
ex:Template1 [ ?a, ?b ] :: BASE .

# This is a template with a pattern containing three instances:
ex:Template2 [ ?a = "String", ?b ] :: {
  ex:Template1 ( "arg1", "arg2" ), 
  ex:Template1 ( "arg3", "arg4" ), 
  ex:Template1 ( "arg5", "arg6" ) } .

# This is a template, which has one annotation, and a pattern containing one instance.
ex:Template [ ?a, ?b ] 
  @@ex:Template2 (ottt:none, 23) 
  :: 
  { ex:Template3 ( true, ex:A ) } .
"""

NAMED_PIZZA = """x
ex:NamedPizza [
  ! owl:Class ?pizza = p:Grandiosa , ?! LUB<owl:NamedIndividual> ?country  , List<owl:Class> ?toppings
  ]
  @@ cross | ex:SomeAnnotationTemplate("asdf", ++("A", "B", "C")),
  @@<http://asdf>("asdf", "asdf", "asdf")
  :: {
     cross | ex:Template1 (?pizza, ++?toppings) ,
     ex:Template2 (1, 2, 4, 5) ,
     <http://Template2.com> ("asdf"^^xsd:string) ,	
     zipMax | ex:Template4 ("asdf"^^xsd:string, ?pizza, ++( "a", "B" )),
     zipMax | ex:Template4 ([], [], [], ++([], []))
  } .
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

    def test_template_extraction_from_pizza_template(self):
        stottr = stOTTR()
        stottr.process(NAMED_PIZZA)
        sut = stottr.templates['ex:NamedPizza']
        assert sut.iri == 'ex:NamedPizza'