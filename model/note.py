from datetime import datetime


class Note:
    __ident = None
    __caption = ""
    __body = ""
    __date_of_creation = datetime.now()
    __date_of_modification = datetime.now()

    def __init__(self, ident, caption, body) -> None:
        self.__ident = ident
        self.__caption = caption
        self.__body = body
        self.__dt_creation = datetime.now()
        self.__date_of_modification = self.__dt_creation
    
    def _set_id(self,id):
        self.__ident = id

    def get_id(self, ident):
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

    def equal(self, other:Note) -> bool:
        return (self.__body == other.get_body() and self.__caption == other.get_caption())

    def __repr__(self):
        return {
            "id": self.__ident,
            "caption": self.__caption,
            "body": self.__body,
            "date_of_creation": self.__date_of_creation,
            "date_of_modification": self.__date_of_modification
        }
