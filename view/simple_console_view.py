from view.absview import Absview


class SimpleConsoleView(Absview):

    def __init__(self, actions):
        self.actions = actions
        self.__prompt()

    def create_record(self):
        record = dict()
        print("Введите заголовок заметки:")
        tinput = input()
        record["caption"] = tinput
        print('-' * 75)
        print("Введите заметку. Для сохранения введите "
              "Ctrl-D (Ctrl-Z в Windows ):")
        record["body"] = self.__multiline_input()
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
        print(
            "Заголовок [Enter оставлляет предыдущее значение]:"
            + record["caption"])
        tinput = input()
        record["caption"] = tinput if tinput != "" else record["caption"]
        print('-' * 75)
        print(
            "Заметка. Для сохранения введите Ctrl-D (Ctrl-Z в Windows):"
            "[оставьте пустым для предыдущего значения]:\n" + record["body"])
        tinput = self.__multiline_input().strip()
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
            return 0
        elif key.isdigit():
            return int(key)
        else:
            return -1

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

    def __multiline_input(self):
        result = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            result.append(line)
        return '\n'.join(result)
