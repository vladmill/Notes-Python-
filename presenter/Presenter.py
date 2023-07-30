class Presenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.view.set_presenter(self)

    def add_note(self):
        self.model.add_note()

    def list(self):
        return self.model.get_list()
    def change(self):
        self.model.ch_note()
    def del_note(self):
        self.model.del_note()