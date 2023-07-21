from model import notebook
import json
from abc import ABC, abstractmethod
from datetime import datetime, date


class BasePresenter(ABC):

    def __init__(self, actions):
        self.notebook = notebook.Notebook()
        self.actions = actions

    def import_notebook(self, path):
        try:
            with open(path, mode='r') as fd:
                notes = json.load(fd, object_hook=self.__deserializer)
                for note in notes:
                    self.notebook.import_note(note)
        except FileNotFoundError:
            # TODO: logfile error record
            print("Ошибка импорта: файл {} не найден".format(path))
        except json.JSONDecodeError:
            print("Ошибка импорта: файл {} сохранен в неверном "
                  "формате".format(path))

    def export_notebook(self, path):
        try:
            with open(path, mode="w") as fd:
                json.dump(
                    [note.to_dict() for note in self.notebook],
                    fd, default=self.__serializer)
        except FileNotFoundError:
            # TODO: logfile error record
            print("Ошибка экспорта: файл {} не найден".format(path))
        except PermissionError:
            # TODO: logfile error record
            print(
                "Ошибка экспорта: недостаточно прав на запись {}".format(path))

    def run(self):
        while True:
            try:
                action = self.view.get_action()
                if action == self.actions.stop.value[0]:
                    break
                elif action == self.actions.nothing.value[0]:
                    continue
                elif action in [
                    action[0] for action in enumerate(self.actions)
                ]:
                    self._action_process(action)
                else:
                    continue
            except IndexError:
                print("Введен несуществующий номер заметки")

    @classmethod
    @abstractmethod
    def _action_process(self, action):
        pass

    def __serializer(self, o):
        if isinstance(o, (date, datetime)):
            return o.strftime('%Y-%m-%d %H:%M:%S')

    def __deserializer(self, o):
        for (key, value) in o.items():
            try:
                o[key] = datetime.strptime(
                    value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                pass
            except TypeError:
                pass
        return o
