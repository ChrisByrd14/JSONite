from jsonite.Transformer import Transformer


class Javascript:

    data = {}
    namespace = "window"
    script_string = "<script>\n{}\n</script>"

    @staticmethod
    def put(data={}):
        Javascript.data.update(data)

    @staticmethod
    def render():
        transformer = Transformer()
        data = [transformer.convert(key, value) for key, value in Javascript.data.items()]
        return Javascript.script_string.format('\n'.join(data))

