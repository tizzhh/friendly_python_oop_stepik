from itertools import count


class Thing:
    _id = count(0)

    def __init__(self, name, price) -> None:
        self.id = next(self._id)
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None

    def get_data(self):
        return self.__dict__.values()


class Table(Thing):
    def __init__(self, name, price, weight, dims) -> None:
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory, frm) -> None:
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm


table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
