from abc import ABC, abstractmethod
import inspect


class Transformer(ABC):
    @abstractmethod
    def convert(self, key, value):
        pass
    
