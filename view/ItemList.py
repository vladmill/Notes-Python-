from view.Item import Item


class ItemList(Item):
    def __init__(self, view):
        self.view = view
        self.description = "Показать все заметки"

    def execute(self):
        self.view.show_list()
