from unittest import TestCase
from pyottr.model import *

class ParameterShould(TestCase):
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


class PrefixShould(TestCase):
    def test_instantiation(self):
        sut = Prefix('l:', 'hello')
        assert sut.label == 'l:'
        assert sut.iri == 'hello'


class StatementsShould(TestCase):
    def test_template_with_no_parameters(self):
        sut = Template('ex:example')
        assert sut.name == 'ex:example'
        assert len(sut.parameters) == 0
        assert str(sut) == 'ex:example [] .'

    def test_template_with_single_parameter(self):
        sut = Template('ex:test')
        sut.add_parameter(Parameter('?pizza'))
        assert sut.name == 'ex:test'
        assert len(sut.parameters) == 1
        assert str(sut) == 'ex:test [ ?pizza ] .'


class TermsShould(TestCase):
    def test_term_equality(self):
        assert Term(1) == Term(1)
        assert Term('a') == Term('a')
        assert Iri('ex:Pizza') == Iri('ex:Pizza')

    def test_term_inequality(self):
        assert Term(1) != Term(2)
        assert Term('a') != Term('b')
        assert Term('abc') != Term(123)
        assert Iri(':Pizza') != Iri('ex:Pizza')