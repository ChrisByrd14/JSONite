from json import dumps, JSONEncoder
import os

from orator import Model


class Encoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Model):
            return obj.__dict__['_original']
        return obj.__dict__


class Transformer:
    """ This is the class that transforms Python variables to Javascript. """

    declaration = '.{} = {};'

    def __init__(self):
        if os.getenv('JS_NAMESPACE'):
            self.declaration = os.getenv('JS_NAMESPACE') + self.declaration
            return
        self.declaration = 'window' + self.declaration

    def convert(self, key, value):
        if isinstance(value, range):
            return self._convert_range(key, value)
        return self.declaration.format(key, Encoder().encode(value))

    def _convert_range(self, key, value):
        return self.declaration.format(key, dumps([x for x in value]))

