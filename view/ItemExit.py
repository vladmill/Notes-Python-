from view.Item import Item


class ItemExit(Item):
    def __init__(self, view):
        self.view = view
        self.description = "Выйти"

    def execute(self):
        self.view.exit()
