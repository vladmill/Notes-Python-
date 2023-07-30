from view.Item import Item


class ItemDel(Item):
    def __init__(self, view):
        self.view = view
        self.description = "Удалить заметку"

    def execute(self):
        self.view.del_note()
