from typing import List


class Cell:
    def __init__(self, data) -> None:
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int) -> None:
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.__table: List[List[Cell]] = [
            [Cell(0) for _ in range(self.cols)] for _ in range(self.rows)
        ]

    def __getitem__(self, indexes):
        x, y = indexes[0], indexes[1]
        self.__check_indexes(x, y)
        return self.__table[x][y].data

    def __setitem__(self, indexes, val):
        x, y = indexes[0], indexes[1]
        self.__check_indexes(x, y)
        self.__check_type(val)
        self.__table[x][y].data = val

    def __iter__(self):
        self._i = 0
        return self

    def __next__(self):
        if self._i < self.rows:
            obj = (x.data for x in iter(self.__table[self._i]))
            self._i += 1
            return obj
        else:
            raise StopIteration

    def __check_type(self, val):
        if not isinstance(val, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')

    def __check_indexes(self, x, y):
        if not 0 <= x < self.rows or not 0 <= y < self.cols:
            raise IndexError('неверный индекс')
