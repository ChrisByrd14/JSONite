import pytest

def test_transformer_import():
    try:
        from py2js.transformers import DictTransformer
        from py2js.transformers import ListTransformer
        from py2js.transformers import TupleTransformer
        from py2js.transformers import RangeTransformer
        from py2js.transformers import StringTransformer
        assert True
    except:
        assert False
