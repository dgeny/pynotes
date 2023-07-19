from model.note import Note


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
