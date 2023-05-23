from unittest import TestCase

from pyottr.model import *


def test_simple_parameter_name():
    assert str(Parameter('?a')) == '?a'
    assert str(Parameter('?b')) == '?b'

def test_optional_parameter():
    sut = Parameter('?name')
    assert str(sut) == '?name'
    sut.set_optional(True)
    assert str(sut) == '??name'

def test_nonempty_parameter():
    sut = Parameter('?x')
    assert str(sut) == '?x'
    sut.set_nonblank(True)
    assert str(sut) == '!?x'

def test_optional_nonempty_parameter():
    sut = Parameter('?hello')
    sut.set_nonblank(True)
    sut.set_optional(True)
    assert str(sut) == '?!?hello'

def test_default_value_parameter():
    sut = Parameter('?withDefault')
    sut.set_default_value('xyz')
    assert str(sut) == '?withDefault = "xyz"'


def test_prefix_instantiation():
    sut = Prefix('l:', 'hello')
    assert sut.label == 'l:'
    assert sut.iri == 'hello'



def test_template_with_no_parameters():
    sut = Template('ex:example')
    assert isinstance(sut.name, Iri)
    assert sut.name == 'ex:example'
    assert len(sut.parameters) == 0
    assert str(sut) == 'ex:example [] .'

def test_template_with_single_parameter():
    sut = Template('ex:test')
    sut.add_parameter(Parameter('?pizza'))
    assert isinstance(sut.name, Iri)
    assert sut.name == 'ex:test'
    assert len(sut.parameters) == 1
    assert str(sut) == 'ex:test [ ?pizza ] .'


def test_term_equality():
    assert Term(1) == Term(1)
    assert Term('a') == Term('a')
    assert Iri('ex:Pizza') == Iri('ex:Pizza')

def test_term_inequality():
    assert Term(1) != Term(2)
    assert Term('a') != Term('b')
    assert Term('abc') != Term(123)
    assert Iri(':Pizza') != Iri('ex:Pizza')