from typing import Union


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self) -> None:
        self.book_list = []

    def __add__(self, other: Book) -> None:
        self.book_list.append(other)
        return self

    def __sub__(self, other: Union[Book, int]) -> None:
        if isinstance(other, Book):
            self.book_list.remove(other)
        elif isinstance(other, int):
            self.book_list.pop(other)
        return self

    def __len__(self) -> int:
        return len(self.book_list)


lib = Lib()
book = Book('aoba', 'aboba', 200)
lib = lib + book  # добавление новой книги в библиотеку
lib += book

lib = (
    lib - book
)  # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = (
    lib - 0
)  # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= 0
n = len(lib)
