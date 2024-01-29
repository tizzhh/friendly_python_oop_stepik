from random import randint
from typing import Any, List


class CellDescr:
    def __set_name__(self, owner, name) -> None:
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, value) -> None:
        setattr(instance, self.name, value)


class Cell:
    is_mine = CellDescr()
    number = CellDescr()
    is_open = CellDescr()

    def __init__(self) -> None:
        self.is_mine = False
        self.number = 0
        self.is_open = False

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['is_mine', 'is_open']:
            if not isinstance(__value, bool):
                raise ValueError("недопустимое значение атрибута")
        if __name == 'number':
            if not isinstance(__value, int) or not 0 <= __value <= 8:
                raise ValueError("недопустимое значение атрибута")
        super().__setattr__(__name, __value)

    def __bool__(self) -> bool:
        return not self.is_open


class GamePole:
    __instance = None

    def __init__(self, N: int, M: int, total_mines: int) -> None:
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells = [
            [Cell() for _ in range(0, self.M)] for _ in range(0, self.N)
        ]

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @property
    def pole(self) -> List[List[Cell]]:
        return self.__pole_cells

    def init_pole(self) -> None:
        mines_left = self.total_mines
        while mines_left:
            x, y = randint(0, self.N - 1), randint(0, self.M - 1)
            if not self.pole[x][y].is_mine:
                self.pole[x][y].is_mine = True
                mines_left -= 1
        self.__set_around_mines()

    def __set_around_mines(self) -> None:
        for i in range(0, self.N):
            for j in range(0, self.M):
                self.pole[i][j].number = self.__count_mines(i, j)

    def __count_mines(self, x: int, y: int) -> int:
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (
                    (i == x and j == y)
                    or i < 0
                    or i >= self.N
                    or j < 0
                    or j >= self.M
                ):
                    continue
                if self.pole[i][j].is_mine:
                    count += 1
        return count

    def open_cell(self, i: int, j: int) -> None:
        if 0 <= i < self.N and 0 <= j < self.M:
            self.pole[i][j].is_open = True
        else:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

    def show_pole(self) -> None:
        for i in range(0, self.N):
            for j in range(0, self.M):
                cell = self.pole[i][j]
                if cell.is_mine:
                    print('* ', end='')
                else:
                    print(f'{cell.number} ', end='')
            print()
