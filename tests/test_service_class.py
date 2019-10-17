import pytest

from jsonite.Javascript import Javascript


from test_transformer import DummyClass


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

def test_data_is_emptied_when_calling_render_function():
    Javascript.data = {'a': 1, 'b': 2}
    assert Javascript.data
    result = Javascript.render()
    assert not Javascript.data

def test_put_method_can_take_an_ambiguous_number_of_arguments():
    dummy = DummyClass()
    Javascript.put({'a': 1, 'b': 2}, an_object=dummy)
    Javascript.put(foo={'c': 3}, bar={'d': 4})
    expected = {
        'a': 1, 'b': 2, 'an_object': dummy, 'foo': {'c': 3}, 'bar': {'d': 4}
    }
    expected_string = '''
<script>
let jsonite.data = {
    "a": 1,
    "b": 2,
    "an_object": {"foo": "bar", "baz": 12345.6},
    "foo": ["c"],
    "bar": ["d"],
}
</script>'''

    assert Javascript.data == expected
    assert Javascript.render() == expected_string.strip()

