from datetime import datetime


class Note:
    __id = None
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
    
    def get_body(self):
        return self.__body

    def set_body(self, body):
        self.__body = body
        self.__date_of_modification = datetime.now()
    
    def get_caption(self):
        return self.__caption

    def get_caption(self, caption):
        self.__caption = caption
        self.__date_of_modification = datetime.now()

    def equal(self, other:Note) -> bool:
        return (self.__body == other.get_body() and self.__caption == other.get_caption())
