from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def save(self, *args, **kwargs):
        pass
