from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, view):
        self.description = None
        self.view = view

    def __str__(self):
        return self.description

    @abstractmethod
    def execute(self):
        pass
