import pytest

from py2js.PythonToJavascript import PythonToJavascript

def test_service_data_is_accessible():
    assert isinstance(PythonToJavascript.data, dict)

def test_put_method_appends_data_to_static_data():
    test_values = { 'a': 1, 'b': 2, 'c': 3, 'foo': 'bar' }
    assert not PythonToJavascript.data  # dictionary is empty
    PythonToJavascript.put(test_values)
    assert PythonToJavascript.data  # dictionary is not empty
    assert PythonToJavascript.data == test_values
