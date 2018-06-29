import inspect
import json
from types import GeneratorType


class Transformer:

    def convert(self, key, value):
        value_type = type(value)

        if isinstance(value, range):
            return self._convert_range(key, value)
        elif inspect.isclass(value):
            return self._convert_class(key, value)
        return "{} = {};".format(key, json.dumps(value))

    def _convert_range(self, key, value):
        return "{} = {};".format(key, json.dumps([x for x in value]))

    def _convert_class(self, key, value):
        pass

