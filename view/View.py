from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def start(self):
        pass
