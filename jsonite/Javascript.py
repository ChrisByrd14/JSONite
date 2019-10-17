from inspect import isclass
import os

from jsonite.Transformer import Transformer


class Javascript:

    data = {}
    script_string = "<script>\nlet {} = {}\n</script>"

    @staticmethod
    def put(*args, **kwargs):  #={}):
        """Add the provided parameters to the Javascript object.

        Examples:
            Javascript.put({'foo': 'bar'})
            Javascript.put(person={'name': 'Jane Doe', 'age': 24})
            Javascript.put(user=user_object)
        """
        for arg in args:
            if isclass(arg):
                arg = {arg.__class__.__name__: arg.__dict__}

            Javascript.data.update(arg)

        for kw in kwargs:
            if isclass(kwargs[kw]):
                kwargs[kw] = kwargs[kw].__dict__
            Javascript.data.update({kw: kwargs[kw]})


    @staticmethod
    def render():
        tran = Transformer()
        data = [tran.convert(k, v) for k, v in Javascript.data.items()]

        identifier = os.getenv('JS_NAMESPACE', 'jsonite') + '.data'
        data_string = '\n    '.join(data)

        result = Javascript.script_string.format(
            identifier, '{\n    ' + data_string + '\n}'
        )

        Javascript.data = dict()
        return result

