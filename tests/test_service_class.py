import pytest

from py2js.Javascript import Javascript


def test_service_data_is_accessible():
    assert isinstance(Javascript.data, dict)


def test_put_method_adds_data_to_static_data():
    test_values = {"a": 1, "b": 2, "c": 3, "foo": "bar"}
    assert not Javascript.data  # dictionary is empty
    Javascript.put(test_values)
    assert Javascript.data  # dictionary is not empty
    assert Javascript.data == test_values


def test_put_method_appends_data_when_static_data_not_empty():
    Javascript.data = {}
    values_1 = {"a": 1, "b": "foo", "c": 3.14, "d": {"var1": 157e10}}
    Javascript.put(values_1)
    values_2 = {"e": "test"}
    Javascript.put(values_2)
    values_1.update(values_2)
    assert Javascript.data == values_1
