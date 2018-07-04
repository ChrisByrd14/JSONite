import os

from py2js.Transformer import Transformer


class DummyClass:
    def __init__(self):
        self.foo = 'bar'
        self.baz = 12345.6


def test_convert_string():
    converted = (Transformer()).convert("foo", "bar")
    assert converted == 'window.foo = "bar";'


def test_convert_list():
    converted = (Transformer()).convert("some_list", [1, 2, 3, 4, 5])
    assert converted == "window.some_list = [1, 2, 3, 4, 5];"


def test_convert_tuple():
    converted = (Transformer()).convert("some_tuple", (1.2, 2.3, 3.14))
    assert converted == "window.some_tuple = [1.2, 2.3, 3.14];"


def test_convert_range():
    converted = (Transformer()).convert("some_range", range(0, 5))
    assert converted == "window.some_range = [0, 1, 2, 3, 4];"


def test_convert_class():
    klass = DummyClass()
    converted = (Transformer()).convert("some_class", klass)
    assert converted == 'window.some_class = {"foo": "bar", "baz": 12345.6};'


def test_namspace():
    os.environ['JS_NAMESPACE'] = 'my_app'
    converted = (Transformer()).convert("some_int", 12)
    assert converted == "my_app.some_int = 12;"

