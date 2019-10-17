
from collections import Iterable
from json import dumps, JSONEncoder
import os

from orator import Model


class Encoder(JSONEncoder):
    """ JSON encoder for class instances.

    Orator models will encode their attributes only
    Any others will encode all fields int their __dict__ attribute
    """

    def default(self, obj):
        if isinstance(obj, Model):
            return obj.__dict__['_original']
        return obj.__dict__


class Transformer:
    """Transforms Python variables to Javascript."""

    declaration = '.{} = {};'

    def __init__(self):
        self.declaration = os.getenv('JS_NAMESPACE', 'window')+self.declaration
        self.encoder = Encoder()

    def convert(self, key, value):
        if isinstance(value, Iterable) and not isinstance(value, str):
            value = list(value)

        return self.declaration.format(key, self.encoder.encode(value))

