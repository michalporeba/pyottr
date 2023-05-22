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
        assert stottr.get_template('ex:EmptyTemplate') is None
        stottr.parse('ex:EmptyTemplate [ ] .')
        assert stottr.get_template('ex:EmptyTemplate') is not None

    # def test_with_spec_example_01(self):
    #     stottr = stOTTR()
    #     stottr.parse('ex:NamedPizza [ ??pizza  ] .')
    #     template = stottr.get_template('ex:NamedPizza')
    #     assert len(template.parameters) == 1
    #     pizza = template.get_parameter('?pizza')
    #     assert pizza.variable == '?pizza'
    #     assert pizza.optional == True 
    #     assert pizza.nonblank == False 
    #     assert pizza.default_value == None

    # def test_with_spec_example_02(self):
    #     stottr = stOTTR()
    #     stottr.parse('ex:NamedPizza [ !?pizza ] .')
    #     template = stottr.get_template('ex:NamedPizza')
    #     pizza = template.get_parameter('?pizza')
    #     assert pizza.variable == '?pizza'
    #     assert pizza.optional == False
    #     assert pizza.nonblank == True
    #     assert pizza.default_value == None

    # def test_with_spec_example_03(self):
    #     stottr = stOTTR()
    #     stottr.parse('ex:NamedPizza [ ?!?pizza ] .')
    #     template = stottr.get_template('ex:NamedPizza')
    #     pizza = template.get_parameter('?pizza')
    #     assert pizza.variable == '?pizza'
    #     assert pizza.optional == True
    #     assert pizza.nonblank == True
    #     assert pizza.default_value == None

    # def test_with_spec_example_04(self):
    #     stottr = stOTTR()
    #     stottr.parse('ex:NamedPizza [ !??pizza ] .')
    #     template = stottr.get_template('ex:NamedPizza')
    #     assert str(template) == 'ex:NamedPizza [ !??pizza ] .'
    #     pizza = template.get_parameter('?pizza')
    #     assert pizza.variable == '?pizza'
    #     assert pizza.optional == True
    #     assert pizza.nonblank == True
    #     assert pizza.default_value == None

    # def test_with_spec_example_05(self):
    #     stottr = stOTTR()
    #     stottr.parse('ex:NamedPizza [ owl:Class ?pizza ] .')
    #     template = stottr.get_template('ex:NamedPizza')
    #     assert str(template) == 'ex:NamedPizza [ owl:Class ?pizza ] .'
    #     pizza = template.get_parameter('?pizza')
    #     assert pizza.variable == '?pizza'
    #     assert pizza.optional == False
    #     assert pizza.nonblank == False
    #     assert pizza.default_value == None

    # def test_error(self):
    #     stottr_input = """
    #     #@prefix : <http://example.xyz/ns> .
    #     #@prefix ex: <http://example.net/ns> .
    #     #PREFIX ex2: <http://example.com/ns>

    #     # modifiers
    #     ex:NamedPizza [ owl:Class ?pizza ] .
    #     #ex:NamedPizzaA [ ??pizza  ] .
    #     #ex:NamedPizzaB [ !?pizza ] .
    #     #ex:NamedPizzaC [ ?!?pizza ] .
    #     #ex:NamedPizzaD [ !??pizza ] .
    #     """
    #     stottr = stOTTR()
    #     (prefixes, templates) = stottr.parse(stottr_input)
    #     print('templates')
    #     print(templates)
    #     assert ''==str(templates)
    #     assert 1 == 0
        

#ex:NamedPizza [ ? owl:Class ?pizza ] .
#ex:NamedPizza [ ?! owl:Class ?pizza ] .