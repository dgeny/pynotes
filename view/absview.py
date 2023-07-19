from abc import ABC, abstractmethod


class Absview(ABC):

    @classmethod
    @abstractmethod
    def show_notebook(self):
        pass

    @classmethod
    @abstractmethod
    def create_record(self):
        pass

    @classmethod
    @abstractmethod
    def show_record(self, record):
        pass

    @classmethod
    @abstractmethod
    def update_record(self, record):
        pass

    @classmethod
    @abstractmethod
    def delete_record(self, recnum):
        pass

    @classmethod
    @abstractmethod
    def select_record(self):
        pass

    @classmethod
    @abstractmethod
    def get_action(self):
        pass
