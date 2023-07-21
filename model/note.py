from datetime import datetime


class Note:

    def __init__(self, ident, caption, body, dt_c=None, dt_m=None) -> None:
        self.__ident = ident
        self.__caption = caption
        self.__body = body
        self.__date_of_creation = dt_c if dt_c else datetime.now()
        self.__date_of_modification = dt_m if dt_m else self.__dt_creation

    def _set_id(self, id):
        self.__ident = id

    def get_id(self):
        return self.__ident

    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body
        self.__date_of_modification = datetime.now()

    def get_caption(self):
        return self.__caption

    def set_caption(self, caption):
        self.__caption = caption
        self.__date_of_modification = datetime.now()

    def get_date_of_creation(self):
        return self.__date_of_creation

    def get_date_of_modification(self):
        return self.__date_of_modification

    def equal(self, other) -> bool:
        return (self.__body == other.get_body()
                and self.__caption == other.get_caption())

    def __str__(self):
        return str.format(
            '{{"id":"{}","caption":"{}","body":"{}","date_of_creation":"{}",'
            '"date_of_modification":"{}" }}',
            self.__ident, self.__caption, self.__body,
            self.__date_of_creation, self.__date_of_modification
        )

    def to_dict(self):
        return {
            "id": self.__ident,
            "caption": self.__caption,
            "body": self.__body,
            "date_of_creation": self.__date_of_creation,
            "date_of_modification": self.__date_of_modification
        }
