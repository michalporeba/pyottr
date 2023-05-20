from unittest import TestCase
from pyottr.model import Parameter, Template

class ModelShould(TestCase):
    def test_simple_parameter_name(self):
        assert str(Parameter('?a')) == '?a'
        assert str(Parameter('?b')) == '?b'

    def test_optional(self):
        sut = Parameter('?name')
        assert str(sut) == '?name'
        sut.set_optional(True)
        assert str(sut) == '??name'

    def test_nonempty(self):
        sut = Parameter('?x')
        assert str(sut) == '?x'
        sut.set_nonblank(True)
        assert str(sut) == '!?x'
    
    def test_optional_nonempty(self):
        sut = Parameter('?hello')
        sut.set_nonblank(True)
        sut.set_optional(True)
        assert str(sut) == '?!?hello'

    def test_default_value(self):
        sut = Parameter('?withDefault')
        sut.set_default_value('xyz')
        assert str(sut) == '?withDefault = "xyz"'

    def test_template_with_no_parameters(self):
        sut = Template('ex:example')
        assert sut.iri == 'ex:example'
        assert len(sut.parameters) == 0
        assert str(sut) == 'ex:example [] .'

    def test_template_with_single_parameter(self):
        sut = Template('ex:test')
        sut.add_parameter(Parameter('?pizza'))
        assert sut.iri == 'ex:test'
        assert len(sut.parameters) == 1
        assert str(sut) == 'ex:test [ ?pizza ] .'