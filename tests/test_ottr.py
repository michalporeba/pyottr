import logging as log

import pytest

from ottrlib.model import Basic, Literal, Prefix, Top, TypedList
from ottrlib.Ottr import Ottr

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

NAMED_PIZZA = """
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
                    "type": Basic("owl:Class"),
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
                    "type": Basic("owl:Class"),
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
                    "type": Basic("owl:Class"),
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
    (
        "ex:Template2 [ ! owl:Class ?a, ? xsd:int ?b = 5 ] .",
        {
            "name": "ex:Template2",
            "parameters": [
                {
                    "variable": "?a",
                    "type": Basic("owl:Class"),
                    "nonblank": True,
                },
                {
                    "variable": "?b",
                    "type": Basic("xsd:int"),
                    "optional": True,
                    "default_value": Literal(5),
                },
            ],
        },
    ),
    (
        "ex:Types [ ! List<xsd:int> ?numbers] .",
        {
            "name": "ex:Types",
            "parameters": [
                {
                    "variable": "?numbers",
                    "type": TypedList(Basic("xsd:int")),
                    "nonblank": True,
                },
            ],
        },
    ),
]


def test_single_minimal_template():
    sut = Ottr()
    assert sut.get_template("ex:EmptyTemplate") is None
    sut.parse("ex:EmptyTemplate [ ] .")
    assert sut.get_template("ex:EmptyTemplate") is not None


@pytest.mark.parametrize("signature,description", TEMPLATES_WITH_PARAMETERS_TEST_DATA)
def test_templates_with_parameters(signature, description):
    log.info(f"parsing {signature}")
    log.info(f"expecting {description}")
    sut = Ottr()
    sut.parse(signature)
    template = sut.get_template(description["name"])
    assert template is not None, f'template {description["name"]} should be found'
    assert len(template.parameters) == len(
        description["parameters"]
    ), f'template should have {len(description["parameters"])} parameters'
    for expected in description["parameters"]:
        actual = template.get_parameter(expected["variable"])
        assert (
            actual.variable == expected["variable"]
        ), f"invalid variable name {actual.variable}"
        assert actual.optional == expected.get(
            "optional", False
        ), "invalid optional value"
        assert actual.nonblank == expected.get(
            "nonblank", False
        ), "invalid nonblank value"
        if expected.get("type", Top()):
            assert actual.type_ == expected.get(
                "type", Top()
            ), f'invalid type of type {expected.get("type")}'
        if expected.get("default_value", None):
            assert actual.default_value == expected.get(
                "default_value", None
            ), f"default value should be {expected.get('default_value')}"


PATTERNS_TEST_DATA = [
    (
        """ex:SinglePatterns [ ?identifier, ?label ] :: {
            ottr:Triple(?identifier, rdfs:label, ?label)
        }.
        """,
        {
            "name": "ex:SinglePatterns",
            "parameters": [
                {"variable": "?identifier"},
                {"variable": "?label"},
            ],
            "patterns": ["ottr:Triple(?identifier, rdfs:label, ?label)"],
        },
    ),
    (
        """ex:MultiplePatterns [ ?identifier, ?label ] :: {
            ottr:Triple(?identifier, rdf:type, owl:Class),
            ottr:Triple(?identifier, rdfs:label, ?label)
        }.
        """,
        {
            "name": "ex:MultiplePatterns",
            "parameters": [
                {"variable": "?identifier"},
                {"variable": "?label"},
            ],
            "patterns": [
                "ottr:Triple(?identifier, rdf:type, owl:Class)",
                "ottr:Triple(?identifier, rdfs:label, ?label)",
            ],
        },
    ),
]


@pytest.mark.parametrize("signature,description", PATTERNS_TEST_DATA)
def test_templates_with_patterns(signature, description):
    log.info(f"parsing = {signature}")
    log.info(f"expecting = {description}")
    sut = Ottr()
    sut.parse(signature)
    template = sut.get_template(description["name"])
    assert template is not None
    assert len(template.instances) == len(description["patterns"])
    assert [str(t) for t in template.instances] == description["patterns"]


DEFAULT_PREFIX_DATA = [
    ("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#"),
    ("rdfs", "http://www.w3.org/2000/01/rdf-schema#"),
    ("owl", "http://www.w3.org/2002/07/owl#"),
    ("xsd", "http://www.w3.org/2001/XMLSchema#"),
    ("ottr", "http://ns.ottr.xyz/0.4/"),
    ("ax", "http://tpl.ottr.xyz/owl/axiom/0.1/"),
    ("rstr", "http://tpl.ottr.xyz/owl/restriction/0.1/"),
    ("ex", "http://example.com/ns#"),
]


@pytest.mark.parametrize("label,iri", DEFAULT_PREFIX_DATA)
def test_default_prefixes(caplog, label, iri):
    caplog.set_level(log.WARNING)
    sut = Ottr()
    prefix = sut.get_prefix(label)
    print(caplog.records)
    assert any([r for r in caplog.records if r.levelno == log.WARNING])
    assert prefix == Prefix(label, iri)
