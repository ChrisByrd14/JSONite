from py2js.transformers import Transformer



def test_convert_string():
    converted = (Transformer()).convert('foo', 'bar')
    assert converted == 'foo = "bar";'

def test_convert_list():
    converted = (Transformer()).convert('some_list', [1, 2, 3, 4, 5])
    assert converted == 'some_list = [1, 2, 3, 4, 5];'

def test_convert_tuple():
    converted = (Transformer()).convert('some_tuple', (1.2, 2.3, 3.14))
    assert converted == 'some_tuple = [1.2, 2.3, 3.14];'

def test_convert_range():
   converted = (Transformer()).convert('some_range', range(0, 5))
   assert converted == 'some_range = [0, 1, 2, 3, 4];'

