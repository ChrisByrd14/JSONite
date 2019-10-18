import os

from jsonite import Transformer


class DummyClass:
    def __init__(self):
        self.foo = 'bar'
        self.baz = 12345.6


def test_convert_string():
    converted = (Transformer()).convert("foo", "bar")
    assert converted == '"foo": "bar",'


def test_convert_list():
    converted = (Transformer()).convert("some_list", [1, 2, 3, 4, 5])
    assert converted == '"some_list": [1, 2, 3, 4, 5],'


def test_convert_iterable():
    converted = (Transformer()).convert("some_tuple", (1.2, 2.3, 3.14))
    assert converted == '"some_tuple": [1.2, 2.3, 3.14],'

    converted = (Transformer()).convert("some_range", range(0, 5))
    assert converted == '"some_range": [0, 1, 2, 3, 4],'


def test_convert_class():
    klass = DummyClass()
    converted = (Transformer()).convert("some_class", klass)
    assert converted == '"some_class": {"foo": "bar", "baz": 12345.6},'

