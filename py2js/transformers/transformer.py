from abc import ABC, abstractmethod

class Transformer(ABC):

    @abstractmethod
    def convert(self, key, value):
        pass
