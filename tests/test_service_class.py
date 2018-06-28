import pytest

from py2js.PythonToJavascript import PythonToJavascript


def test_service_data_is_accessible():
    assert isinstance(PythonToJavascript.data, dict)

def test_put_method_adds_data_to_static_data():
    test_values = { 'a': 1, 'b': 2, 'c': 3, 'foo': 'bar' }
    assert not PythonToJavascript.data  # dictionary is empty
    PythonToJavascript.put(test_values)
    assert PythonToJavascript.data  # dictionary is not empty
    assert PythonToJavascript.data == test_values

def test_put_method_appends_data_when_static_data_not_empty():
    PythonToJavascript.data = {}
    values_1 = {'a': 1, 'b': 'foo', 'c': 3.14, 'd': { 'var1': 157e10 } }
    PythonToJavascript.put(values_1)
    values_2 = {'e': 'test'}
    PythonToJavascript.put(values_2)
    values_1.update(values_2)
    assert PythonToJavascript.data == values_1
