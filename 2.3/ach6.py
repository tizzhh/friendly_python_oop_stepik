class FloatValue:
    @classmethod
    def check_val(cls, val):
        if not isinstance(val, float):
            raise TypeError(
                "Присваивать можно только вещественный тип данных."
            )

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check_val(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0) -> None:
        self.value = value


class TableSheet:
    def __init__(self, N, M) -> None:
        self.N = N
        self.M = M
        self.cells = [[Cell(0.0) for j in range(0, M)] for i in range(0, N)]


table = TableSheet(5, 3)
for i in range(0, len(table.cells)):
    for j in range(0, len(table.cells[i])):
        table.cells[i][j].value = float(1 + i * table.M + j)
