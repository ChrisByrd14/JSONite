
from collections import Iterable
from inspect import isclass
from json import dumps, JSONEncoder
from os import getenv as env

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
        # self.declaration = env('JS_NAMESPACE', 'jsonite') + self.declaration
        self.declaration = '"{}": {},'
        self.encoder = Encoder()

    def convert(self, key, value):
        if isinstance(value, Iterable) and not isinstance(value, str):
            value = list(value)

        return self.declaration.format(key, self.encoder.encode(value))

