#!/usr/bin/env python3
from presenter.simple_console_presenter import SimpleConsolePresenter
import argparse
from os import path 


def main(dbpath):
    presenter = SimpleConsolePresenter()
    if path.exists(dbpath):
        presenter.import_notebook(dbpath)
    presenter.run()
    presenter.export_notebook(dbpath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='Noter',
                    description='Программа-интерфейс для работы с заметками.\n'
                                'В настоящее время поддерживаются '
                                'автоматические  загрузка/сохранение данных '
                                'в формате JSON (имя файла можно выбрать при '
                                'запуске указав параметр командной строки.',
                    epilog='Разработано в качестве контрольного задания '
                           'в период обучения в GeekBrains')
    parser.add_argument(
        '--db', type=str, help='путь к файлу с сохраненными заметками '
                               '[по умолчанию - notes.json в текущем каталоге]')
    args = parser.parse_args()
    main(args.db if args.db else "notes.json")
