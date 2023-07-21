from utils.supported_actions import ConsoleAction as Action
from presenter.base_presenter import BasePresenter
from view.simple_console_view import SimpleConsoleView
from datetime import datetime


class SimpleConsolePresenter(BasePresenter):

    def __init__(self):
        super().__init__(Action)
        values = [action[1].value[1] for action in enumerate(Action)]
        self.view = SimpleConsoleView(values)

    def _action_process(self, action):
        if action == Action.listing.value[0]:
            self.__show_list(self.notebook)
        elif action == Action.read.value[0]:
            self.__show_one()
        elif action == Action.create.value[0]:
            self.__create()
        elif action == Action.update.value[0]:
            self.__update()
        elif action == Action.delete.value[0]:
            self.__delete()
        elif action == Action.date_filter.value[0]:
            self.__filterby_date()

    def __show_list(self, nb):
        self.view.show_notebook(
            [{
                "id": note.get_id(),
                "caption": note.get_caption(),
                "body": note.get_body()
            } for note in nb]
        )

    def __show_one(self):
        self.view.show_record(
            self.notebook.read_note(
                self.view.select_record()).to_dict())

    def __create(self):
        created = self.view.create_record()
        self.notebook.create_note(
            created["body"], created["caption"])

    def __update(self):
        updated = self.view.update_record(
            self.notebook.read_note(
                self.view.select_record()).to_dict())
        self.notebook.update_note(
            updated["id"], updated["caption"], updated["body"])

    def __delete(self):
        deleting = self.view.select_record()
        if self.view.delete_record(deleting):
            self.notebook.delete_note(deleting)

    def __filterby_date(self):
        date_start, date_end, filter_type = self.view.filterby_date()
        date_start = self.__parse_datetime(date_start)
        date_end = self.__parse_datetime(date_end)

        if filter_type and filter_type.isdigit():
            if int(filter_type) in range(1, 3):
                filter_type = int(filter_type)
            else:
                filter_type = 3
        else:
            filter_type = 3

        notes = self.notebook.filterby_date(
            date_start, date_end, filter_type)
        self.__show_list(notes)

    def __parse_datetime(self, o):
        try:
            return datetime.strptime(o, '%Y-%m-%d')
        except ValueError:
            return None
