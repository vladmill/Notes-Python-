from view.Item import Item


class ItemAdd(Item):
    def __init__(self, view):
        self.view = view
        self.description = "Добавить заметку"

    def execute(self):
        self.view.add()
