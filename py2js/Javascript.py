from py2js.Transformer import Transformer


class Javascript:

    data = {}
    namespace = "window"
    script_string = "<script>{}</script>"

    @staticmethod
    def put(data={}):
        Javascript.data.update(data)

    @staticmethod
    def render():
        pass
