from datetime import datetime, date


class Note:
    def __init__(self, date_note, title_note, txt_note, id_note):
        self.date = date_note
        self.title = title_note
        self.txt = txt_note
        self.id = id_note

    def __str__(self):
        return f"Дата: {self.date}\nЗаголовок: {self.title}\nЗаметка: {self.txt}\nID: {self.id}\n" \
               f"-----------------"

    def class_to_dict(self, obj):
        return obj.__dict__
