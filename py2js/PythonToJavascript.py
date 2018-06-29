from py2js.transformers import Transformer, ClassTransformer


class PythonToJavascript:

    data = {}
    script_string = "<script>{}</script>"

    @staticmethod
    def put(data={}):
        PythonToJavascript.data.update(data)
