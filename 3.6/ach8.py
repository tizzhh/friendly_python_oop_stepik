import sys


class BookStudy:
    def __init__(self, name: str, author: str, year: int) -> None:
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.author.lower()))


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = [BookStudy(*line.split('; ')) for line in lst_in]
unique = set()
unique_books = 0
for book in lst_bs:
    if hash(book) not in unique:
        unique.add(hash(book))
        unique_books += 1
