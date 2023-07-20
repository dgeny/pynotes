from enum import Enum


class ConsoleAction(Enum):
    stop = 0, "q. Выход",
    listing = 1, "1. Показать список заметок",
    read = 2, "2. Подробнее о заметке",
    create = 3, "3. Новая заметка",
    update = 4, "4. Редактировать заметку",
    delete = 5, "5. Удалить заметку",
    nothing = -1, ""
