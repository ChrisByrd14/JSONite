from py2js.transformers import (
    DictTransformer,
    ListTransformer,
    TupleTransformer,
)

class PythonToJavascript:

    data = {}
    script_string = '<script>{}</script>'

    @staticmethod
    def put(data={}):
        PythonToJavascript.data.update(data)
