from typing import Any


class Book:
    def __init__(self, title='', author='', pages=0, year=0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['title', 'author']:
            if not isinstance(__value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
        elif __name in ['pages', 'year']:
            if not isinstance(__value, int):
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(__name, __value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
