import absview
import sys


class SimpleConsoleView(absview.Absview):

    def __init__(self, actions):
        self.actions = actions
        self.__prompt()

    def create_record(self):
        record = dict()
        print("Введите заголовок заметки:")
        tinput = input()
        record["caption"] = tinput
        print('-' * 75)
        print("Введите заметку: ")
        tinput = input()
        record["body"] = tinput
        return record

    def show_record(self, record: dict) -> None:
        self.__prompt()
        print("Note #" + str(record["id"]))
        print(str.format(
            "Creation date:{}\tModification date:{}",
            record["date_of_creation"],
            record["date_of_modification"]))
        print('-' * 75)
        print("Caption:\t" + record["caption"])
        print('-' * 75)
        print(record["body"])

    def update_record(self, record: dict) -> dict:
        print(str.format(
            "Дата создания:{}\tДата изменения:{}",
            record["date_of_creation"],
            record["date_of_modification"]))
        print('-' * 75)
        print("Заголовок [ввод оставлляет предыдущее значение]:" + record["caption"])
        tinput = input()
        record["caption"] = tinput if tinput != "" else record["caption"]
        print('-' * 75)
        print("Заметка [ввод оставлляет предыдущее значение]: " + record["body"])
        tinput = input()
        record["body"] = tinput if tinput != "" else record["body"]
        return record

    def delete_record(self, ident: int) -> bool:
        key = input("Подтвердите удаление записи [{}]: ".format(ident))
        return key.isdigit() and int(key) == ident

    def show_notebook(self, nb: list) -> None:
        self.__prompt()
        self.__printTable(nb)

    def select_record(self) -> int:
        msg = 'Введите номер заметки: '
        result = input(msg)
        while not result.isdigit():
            print('Введены некорректные данные. Попробуйте еще раз.')
            result = input(msg)
        return int(result)

    def get_action(self) -> int:
        key = input('Введите действие: ')
        if key == 'q':
            return -1
        elif key.isdigit():
            return int(key)
        else:
            return 0

    def __printTable(self, notebook):
        myList = [["id", "Caption", "Body"]]  # header

        for note in notebook:
            noteid = str(note["id"])
            caption = str.ljust(note["caption"], 15)
            body = note["body"].split('\n')
            if len(body) > 1:
                myList.append(
                    [noteid, caption, str.ljust(body[0], 55)]
                )
                for line in body[1:]:
                    myList.append(["", "", line])
            else:
                myList.append(
                    [noteid, caption, str.ljust(body[0], 55)]
                )
        colSize = [max(map(len, col)) for col in zip(*myList)]

        # set record sep
        myList.insert(0, ['-' * i for i in colSize])
        pos = 1
        while pos < len(myList):
            if pos + 1 < len(myList) and myList[pos+1][0] == "":
                pos = pos + 1
                continue
            myList.insert(pos+1, ['-' * i for i in colSize])
            pos = pos + 2

        formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
        formatSep = '-+-'.join(["{{:<{}}}".format(i) for i in colSize])
        for item in myList:
            if len(item[0]) > 0 and item[0][0] == '-':
                print(formatSep.format(*item))
            else:
                print(formatStr.format(*item))

    def __prompt(self):
        print("\033[H\033[J", end="")
        print("  ".join(self.actions))


if __name__ == "__main__":
    # import sys
    sys.path.append(
        '/home/tpuser/work/education/checkpoints/python_notes/pynotes')
    from model.notebook import Notebook
    from enum import Enum

    class Actions(Enum):
        showall = 1,

    supported_actions = [
        "1. Показать список заметок",
        "2. Подробнее о заметке",
        "3. Новая заметка",
        "4. Редактировать заметку",
        "5. Удалить заметку",
        "q. Выход"
    ]
    conview = SimpleConsoleView(supported_actions)
    notes = Notebook()
    notes.create_note(
        "Note1\nmy multiline note!. More 30 symbols length."
        " Very hard to display.",
        "1"
    )
    notes.create_note("Note2", "2")
    notes.create_note("Note3", "3")

    while True:
        try:
            action = conview.get_action()
            if action == -1:
                break
            elif action == 0:
                continue
            elif action == 1:
                conview.show_notebook(
                    [{
                        "id": note.get_id(),
                        "caption": note.get_caption(),
                        "body": note.get_body()
                    } for note in notes]
                )
            elif action == 2:
                conview.show_record(
                    notes.read_note(conview.select_record()).to_dict())
            elif action == 3:
                created = conview.create_record()
                notes.create_note(created["body"], created["caption"])
            elif action == 4:
                updated = conview.update_record(
                    notes.read_note(conview.select_record()).to_dict())
                notes.update_note(
                    updated["id"], updated["caption"], updated["body"])
            elif action == 5:
                deleting = conview.select_record()
                if conview.delete_record(deleting):
                    notes.delete_note(deleting)
            else:
                continue
        except IndexError:
            print("Введен несуществующий номер заметки")
