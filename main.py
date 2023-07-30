from model.Model import Model
from presenter.Presenter import Presenter
from view.ViewConsole import ViewConsole

if __name__ == '__main__':
    console = ViewConsole()
    model = Model()
    presenter = Presenter(console, model)
    console.start()
