from typing import Callable, List, Tuple, Union


def check_index(func: Callable) -> Callable:
    def wrapper(self, *args, **kwargs):
        coords = args[0]
        x, y = coords[0], coords[1]
        if not 0 <= x < self.rows or not 0 <= y < self.cols:
            raise IndexError("Индексы за пределами таблицы")
        return func(self, *args, **kwargs)

    return wrapper


class BaseDescr:
    data_type = None
    err_msg = ''

    def __set_name__(self, owner: object, name: str) -> None:
        self.name = f'_{owner.__name__}_{name}'

    def __get__(self, instance: object, owner: object) -> int:
        return getattr(instance, self.name)

    def __set__(self, instance: object, value: int) -> None:
        if not isinstance(value, self.data_type):
            raise ValueError(self.err_msg)
        setattr(instance, self.name, value)


class IntegerValue(BaseDescr):
    data_type = int
    err_msg = 'возможны только целочисленные значения'


class StringValue(BaseDescr):
    data_type = str
    err_msg = 'возможны только строковые значения'


class CellBase:
    value = BaseDescr()
    default_val = None

    def __init__(self, start_value: Union[int, str] = None) -> None:
        self.value = start_value or self.default_val


class CellString(CellBase):
    value = StringValue()
    default_val = ''


class CellInteger(CellBase):
    value = IntegerValue()
    default_val = 0


class TableValues:
    def __init__(
        self, rows: int, cols: int, cell: Union[CellInteger, CellString] = None
    ) -> None:
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.rows = rows
        self.cols = cols
        self.cells: List[List[CellInteger]] = [
            [cell() for _ in range(cols)] for _ in range(rows)
        ]

    @check_index
    def __getitem__(self, coords: Tuple[int]) -> Union[int, str]:
        x, y = coords[0], coords[1]
        return self.cells[x][y].value

    @check_index
    def __setitem__(self, coords: Tuple[int], val: Union[int, str]) -> None:
        x, y = coords[0], coords[1]
        self.cells[x][y].value = val


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()


table = TableValues(2, 3, cell=CellString)
print(table[0, 1])
table[1, 1] = 'aboba'
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
