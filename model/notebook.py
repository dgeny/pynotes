from model.note import Note
from datetime import datetime


class Notebook:
    __notes = list()
    __current = -1

    def __init__(self):
        self.__notes = list()

    def __newid(self) -> int:
        return len(self.__notes)

    def create_note(self, body, caption="Unnamed note"):
        self.__notes.append(Note(self.__newid(), caption, body))
        return self.__notes[len(self.__notes) - 1]

    def read_note(self, ident):
        readed = self.__get_by_id(ident)
        if not readed:
            raise IndexError()
        return readed

    def update_note(self, ident, caption, body):
        updated_note = self.__get_by_id(ident)
        if caption:
            updated_note.set_caption(caption)
        if body:
            updated_note.set_body(body)

    def delete_note(self, ident):
        item_to_delete = self.__get_by_id(ident)
        if item_to_delete:
            self.__notes.remove(item_to_delete)
            self.__reindex()
        else:
            raise IndexError

    def import_note(self, note_dict):
        self.__notes.append(Note(
            note_dict["id"], note_dict["caption"], note_dict["body"],
            note_dict["date_of_creation"], note_dict["date_of_modification"]
        ))
        self.__reindex()

    def filterby_date(
            self, date_start=datetime.min, date_end=datetime.max, date_type=2):
        if not date_start:
            date_start = datetime.min
        if not date_end:
            date_end = datetime.now()
        result = list()
        if date_type == 1:  # date_of_creation
            result = [
                note for note in self
                if note.get_date_of_creation() >= date_start and
                note.get_date_of_creation() <= date_end
            ]
        elif date_type == 2:  # date_of_modification
            result = [
                note for note in self
                if note.get_date_of_modification() >= date_start and
                note.get_date_of_modification() <= date_end
            ]
        else:
            result = [
                note for note in self
                if (note.get_date_of_modification() >= date_start or
                    note.get_date_of_creation() >= date_start) and
                note.get_date_of_modification() <= date_end
            ]
        return result

    def __reindex(self) -> None:
        for ident in range(len(self.__notes) - 1):
            self.__notes[ident]._set_id(ident)

    def __get_by_id(self, ident) -> Note:
        for note in self.__notes:
            if note.get_id() == ident:
                return note
        return None

    def __iter__(self):
        self.__current = 0
        return self
        # return self.__notes[self.__current]

    def __next__(self):
        if self.__current == len(self.__notes):
            raise StopIteration
        x = self.__notes[self.__current]
        self.__current += 1
        return x

    def __repr__(self):
        return str.format("Notebook, {} notes", len(self.__notes))
