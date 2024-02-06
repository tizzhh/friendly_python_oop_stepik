class Book:
    def __init__(self, title, author, pages, year) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm) -> None:
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm
