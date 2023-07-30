from view.Menu import Menu
from view.View import View


class ViewConsole(View):

    def __init__(self):
        self.presenter = None
        self.menu = Menu(self)
        self.work = True

    def set_presenter(self, presenter):
        self.presenter = presenter

    def start(self):
        while self.work:
            self.menu.show_menu()

    def add(self):
        self.presenter.add_note()

    def show_list(self):
        lst = self.presenter.list()
        for note in lst:
            print(note)
    def change_note(self):
        self.presenter.change()
    def del_note(self):
        self.presenter.del_note()

    def exit(self):
        self.work = False
        print("Работа завершена.")
