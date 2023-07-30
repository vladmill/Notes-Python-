from datetime import datetime, date

from model.Note import Note
from model.WriterJSON import WriterJSON


class Model:
    def __init__(self):
        self.writer = WriterJSON()
        self.writer.set_model(self)
        self.notes = []
        self.json_to_note()


    def json_to_note(self):
        self.notes = []
        r = self.writer.read()
        if r is not None:
            for note in r:
                self.notes.append(Note(note["date"], note["title"], note["txt"], note["id"]))
        else:
            print(self.notes)

    def add_note(self):
        date_note = f"{date.today()}"
        title_note = input("Введите заголовок: ")
        txt_note = input("Введите текст заметки: ")
        id_note = ""
        n = Note(date_note, title_note, txt_note, id_note)
        if n.id == "":
            n.id = f"{id(n)}"
        self.writer.save(n, -1)

    def get_list(self):
        self.json_to_note()
        return self.notes

    def get_note(self):
        date_note = input("Дата заметки (ГГГГ-ММ-ДД): ")
        title_note = input("Заголовок заметки: ")
        self.json_to_note()
        for note in self.notes:
            if note.date == date_note and note.title == title_note:
                return note
        return None

    def ch_note(self):
        cur_note = self.get_note()
        if cur_note is None:
            print("Заметка не найдена. Попробуйте еще раз.")
        else:
            newtxt = input("Новый текст заметки: ")
            cur_note.txt = newtxt
            self.writer.save(cur_note, -999)
    def del_note(self):
        cur_note = self.get_note()
        if cur_note is None:
            print("Заметка не найдена. Попробуйте еще раз.")
        else:
            self.writer.save(cur_note, self.notes.index(cur_note))


