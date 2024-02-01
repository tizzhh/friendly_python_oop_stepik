from typing import Callable, Tuple, Union

VALUE_DEFAULT = 0
VALUE_X = 1
VALUE_O = 2
POLE_SIZE = 3


def check_indx(func: Callable) -> Callable:
    def wrapper(self, *args, **kwargs) -> Union[int, None]:
        indxes = args[0]
        if not all(isinstance(x, (int, slice)) for x in indxes):
            raise TypeError("индекс должен быть либо int, либо slice")
        int_indexes = tuple(filter(lambda x: isinstance(x, int), indxes))
        for index in int_indexes:
            if not 0 <= index < POLE_SIZE:
                raise IndexError('неверный индекс клетки')
        return func(self, *args, **kwargs)

    return wrapper


class Cell:
    def __init__(self) -> None:
        self.is_free = True
        self.value = VALUE_DEFAULT

    def __bool__(self) -> bool:
        return self.is_free


class TicTacToe:
    def __init__(self) -> None:
        self.pole = [
            [Cell() for _ in range(POLE_SIZE)] for _ in range(POLE_SIZE)
        ]

    def clear(self) -> None:
        for row in self.pole:
            for cell in row:
                cell.is_free = True
                cell.value = VALUE_DEFAULT

    @check_indx
    def __getitem__(self, indx: Tuple[int]) -> int:
        x, y = indx[0], indx[1]
        if isinstance(x, int) and isinstance(y, int):
            return self.pole[x][y].value
        elif isinstance(x, slice):
            return tuple(self.pole[i][y].value for i in range(POLE_SIZE))
        return tuple(int(cell.value) for cell in self.pole[x][y])

    @check_indx
    def __setitem__(self, indx: Tuple[int], val: int) -> None:
        x, y = indx[0], indx[1]
        cell = self.pole[x][y]
        if not cell:
            raise ValueError('клетка уже занята')
        cell.value = val

    def __str__(self) -> str:
        res = ''
        for row in self.pole:
            for cell in row:
                res += str(cell.value) + ' '
            res += '\n'
        return res
