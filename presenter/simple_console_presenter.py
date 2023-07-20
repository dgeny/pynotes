from utils.supported_actions import ConsoleAction as Action
from presenter.base_presenter import BasePresenter
from view.simple_console_view import SimpleConsoleView


class SimpleConsolePresenter(BasePresenter):

    def __init__(self):
        super().__init__(Action)
        values = [action[1].value[1] for action in enumerate(Action)]
        self.view = SimpleConsoleView(values)

    def _action_process(self, action):
        if action == Action.listing.value[0]:
            self.view.show_notebook(
                [{
                    "id": note.get_id(),
                    "caption": note.get_caption(),
                    "body": note.get_body()
                } for note in self.notebook]
            )
        elif action == Action.read.value[0]:
            self.view.show_record(
                self.notebook.read_note(
                    self.view.select_record()).to_dict())
        elif action == Action.create.value[0]:
            created = self.view.create_record()
            self.notebook.create_note(
                created["body"], created["caption"])
        elif action == Action.update.value[0]:
            updated = self.view.update_record(
                self.notebook.read_note(
                    self.view.select_record()).to_dict())
            self.notebook.update_note(
                updated["id"], updated["caption"], updated["body"])
        elif action == Action.delete.value[0]:
            deleting = self.view.select_record()
            if self.view.delete_record(deleting):
                self.notebook.delete_note(deleting)
