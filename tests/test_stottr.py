import pytest

from pyottr.model import Basic
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

TEMPLATES_WITH_PARAMETERS_TEST_DATA = [
    (
        "ex:NamedPizza [ ??pizza ] .",
        {
            "name": "ex:NamedPizza",
            "parameters": [
                {
                    "variable": "?pizza",
                    "optional": True,
                    "nonblank": False,
                }
            ],
        },
    ),
    (
        "ex:NamedPizza [ !?pizza ] .",
        {
            "name": "ex:NamedPizza",
            "parameters": [
                {
                    "variable": "?pizza",
                    "optional": False,
                    "nonblank": True,
                }
            ],
        },
    ),
    (
        "ex:NamedPizza [ ?!?pizza ] .",
        {
            "name": "ex:NamedPizza",
            "parameters": [
                {
                    "variable": "?pizza",
                    "optional": True,
                    "nonblank": True,
                }
            ],
        },
    ),
    (
        "ex:NamedPizza [ !??pizza ] .",
        {
            "name": "ex:NamedPizza",
            "parameters": [
                {
                    "variable": "?pizza",
                    "optional": True,
                    "nonblank": True,
                }
            ],
        },
    ),
    (
        "ex:NamedPizza [ owl:Class ?pizza ] .",
        {
            "name": "ex:NamedPizza",
            "parameters": [
                {
                    "variable": "?pizza",
                    "types_type": Basic,
                    "type": "owl:Class",
                }
            ],
        },
    ),
    (
        "ex:NamedPizza [ ? owl:Class ?pizza ] .",
        {
            "name": "ex:NamedPizza",
            "parameters": [
                {
                    "variable": "?pizza",
                    "types_type": Basic,
                    "type": "owl:Class",
                    "optional": True,
                }
            ],
        },
    ),
    (
        "ex:NamedPizza [ !? owl:Class ?pizza ] .",
        {
            "name": "ex:NamedPizza",
            "parameters": [
                {
                    "variable": "?pizza",
                    "types_type": Basic,
                    "type": "owl:Class",
                    "optional": True,
                    "nonblank": True,
                }
            ],
        },
    ),
    (
        "ex:Template1 [ ?a , ?b ] .",
        {
            "name": "ex:Template1",
            "parameters": [
                {"variable": "?a"},
                {"variable": "?b"},
            ],
        },
    ),
]


def test_single_minimal_template():
    stottr = stOTTR()
    assert stottr.get_template("ex:EmptyTemplate") is None
    stottr.parse("ex:EmptyTemplate [ ] .")
    assert stottr.get_template("ex:EmptyTemplate") is not None


@pytest.mark.parametrize("representation,expected", TEMPLATES_WITH_PARAMETERS_TEST_DATA)
def test_templates_with_parameters(representation, expected):
    print(f"parsing {representation}")
    print(f"expecting {expected}")
    stottr = stOTTR()
    stottr.parse(representation)
    template = stottr.get_template(expected["name"])
    assert template is not None, f'template {expected["name"]} should be found'
    assert len(template.parameters) == len(
        expected["parameters"]
    ), f'template should have {len(expected["parameters"])} parameters'
    for expected_parameter in expected["parameters"]:
        actual = template.get_parameter(expected_parameter["variable"])
        assert (
            actual.variable == expected_parameter["variable"]
        ), f"invalid variable name {actual.variable}"
        assert actual.optional == expected_parameter.get(
            "optional", False
        ), "invalid optional value"
        assert actual.nonblank == expected_parameter.get(
            "nonblank", False
        ), "invalid nonblank value"
        assert actual.default_value == expected_parameter.get(
            "default", None
        ), f'invalid default value {expected_parameter.get("default", None)}'
        assert actual.type_ == expected_parameter.get(
            "type", None
        ), f'invalid type {expected_parameter.get("type", None)}'
        if expected_parameter.get("types_type", None):
            assert isinstance(
                actual.type_, expected_parameter.get("types_type", None)
            ), f'invalid type of type {expected_parameter.get("types_type")}'
