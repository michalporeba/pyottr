from unittest import TestCase
from pyottr.model import Parameter

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