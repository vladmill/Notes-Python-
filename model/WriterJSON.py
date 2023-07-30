import json
import os

from model.Note import Note
from model.Writer import Writer


class WriterJSON(Writer):

    def __init__(self):
        self.model = None
        self.file = "notes.json"
        self.data = []
    def set_model(self,model):
        self.model = model
    def read(self):
        with open(self.file, encoding="utf-8") as file:
            string = file.read().strip()

        if not string:
            with open(self.file, "w", encoding="utf-8") as file:
                json.dump([], file)

        with open(self.file, encoding="utf-8") as file:
            return json.load(file)

    def save(self, note, i):
        self.data = []
        self.data = self.read()
        if i == -1:
            self.data.append(note)
        elif i >=0:
            self.data.pop(i)
        elif i == -999:
            self.data = self.model.notes

        with open(self.file, "w", encoding="utf-8") as fh:
            json.dump(self.data, fh, ensure_ascii=False, indent=4, default=note.class_to_dict)
        print("Cохранено.")
