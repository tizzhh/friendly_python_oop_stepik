from typing import Any


class LessonItem:
    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['practices', 'duration']:
            if not isinstance(__value, int):
                raise TypeError("Неверный тип присваиваемых данных.")
        if __name == 'title':
            if not isinstance(__value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(__name, __value)

    def __getattr__(self, __item) -> bool:
        return False

    def __delattr__(self, __name: str) -> None:
        raise AttributeError(f"Атрибут {__name} удалять запрещено.")


class Module:
    def __init__(self, name: str) -> None:
        self.name = name
        self.lessons: list[LessonItem] = []

    def add_lesson(self, lesson: LessonItem) -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.modules = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)


course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
