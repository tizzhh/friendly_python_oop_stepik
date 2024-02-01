from typing import Any, Dict, Tuple


class Cell:
    def __init__(self, value: Any) -> None:
        self.value = value


class SparseTable:
    def __init__(self) -> None:
        self.table: Dict[Tuple[int], Cell] = {}

    def __getitem__(self, indexes: Tuple[int]) -> Cell:
        if indexes not in self.table:
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.table[indexes]

    def __setitem__(self, indexes: Tuple[int], new_cell: Cell) -> None:
        self.table[indexes] = new_cell

    def add_data(self, row: int, col: int, data: Cell) -> None:
        self.table[(row, col)] = data

    def remove_data(self, row: int, col: int):
        if (row, col) not in self.table:
            raise IndexError('ячейка с указанными индексами не существует')
        del self.table[(row, col)]

    @property
    def rows(self) -> int:
        return max(self.table, key=lambda x: x[0])[0] + 1 if self.table else 0

    @property
    def cols(self) -> int:
        return max(self.table, key=lambda x: x[1])[1] + 1 if self.table else 0


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
print(st.table)
st[2, 5] = 25  # изменение значения существующей ячейки
st[11, 7] = 'cell_117'  # создание новой ячейки
print(st[0, 0])  # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols)  # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError
