from view.Item import Item


class ItemCh(Item):
    def __init__(self, view):
        self.view = view
        self.description = "Изменить заметку"

    def execute(self):
        self.view.change_note()
