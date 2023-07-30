from view.ItemAdd import ItemAdd
from view.ItemCh import ItemCh
from view.ItemExit import ItemExit
from view.ItemList import ItemList
from view.itemDel import ItemDel


class Menu():
    def __init__(self, view):
        self.view = view
        self.items = []
        self.items.append(ItemAdd(view))
        self.items.append(ItemList(view))
        self.items.append(ItemCh(view))
        self.items.append(ItemDel(view))
        self.items.append(ItemExit(view))

    def show_menu(self):
        for i in range(len(self.items)):
            print(f"{i + 1}. {self.items[i]}")
        n = int(input("Введите номер команды: "))
        print("-----------------")
        self.items[n - 1].execute()