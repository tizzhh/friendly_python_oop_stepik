from random import randint
from typing import Callable, List, Set, Tuple, Union


class Ship:
    WATER = 0
    NOT_HIT = 1
    HIT = 2

    TP_Y_COORD = 1
    TP_X_COORD = 2

    def __init__(
        self, length: int, tp: int = TP_Y_COORD, y: int = None, x: int = None
    ) -> None:
        self._length = length
        self._tp = tp
        self._y = y
        self._x = x
        self._is_move = True
        self._cells = [self.NOT_HIT for _ in range(length)]
        self._ship_cords = self._get_ship_coords()
        self._all_coords = self._get_all_coords()

    @staticmethod
    def _get_set_items_check_args(func: Callable) -> Callable:
        def wrapper(self: 'Ship', *args, **kwargs):
            indx = args[0]
            if not isinstance(indx, int):
                raise TypeError('Indey should be int')
            if not 0 <= abs(indx) < len(self._cells):
                raise IndexError('Indey out or range')
            if len(args) == 2:
                val = args[1]
                if val not in [self.HIT, self.NOT_HIT]:
                    raise ValueError('Wrong value, should be 1 or 2')
            return func(self, *args, **kwargs)

        return wrapper

    @_get_set_items_check_args
    def __getitem__(self, indx: int):
        return self._cells[indx]

    @_get_set_items_check_args
    def __setitem__(self, indx: int, value: int):
        self._cells[indx] = value

    def __repr__(self) -> str:
        return f'{self._y} {self._x}'

    def set_start_coords(self, y: int, x: int) -> None:
        if not isinstance(y, int) or not isinstance(x, int):
            raise TypeError('Coords should be int')
        self._y = y
        self._x = x
        self._ship_cords = self._get_ship_coords()
        self._all_coords = self._get_all_coords()

    def get_start_coords(self) -> Tuple[int]:
        return (self._y, self._x)

    def move(self, go: int) -> None:
        if self._is_move:
            if self._tp == self.TP_Y_COORD:
                self._y += go
            elif self._tp == self.TP_X_COORD:
                self._x += go

    def is_collide(self, ship: 'Ship') -> bool:
        return self != ship and bool(
            set(self._all_coords) & set(ship._all_coords)
        )

    def is_out_pole(self, siye: int) -> bool:
        return not (
            0 <= self._y < siye
            and 0 <= self._x < siye
            and (
                0 <= self._y + self._length - 1 < siye
                if self._tp == self.TP_Y_COORD
                else 0 <= self._x + self._length - 1 < siye
            )
        )

    def _get_all_coords(self) -> Set[Tuple[int]]:
        res = set()
        for y, x in self._ship_cords:
            if y is not None and x is not None:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_i, new_j = y + i, x + j
                        res.add((new_i, new_j))
        return res

    def _get_ship_coords(self) -> List[Tuple[int]]:
        res = []
        if self._y is not None and self._x is not None:
            if self._tp == self.TP_Y_COORD:
                res = [
                    (self._y + step, self._x)
                    for step in range(0, self._length)
                ]
            else:
                res = [
                    (self._y, self._x + step)
                    for step in range(0, self._length)
                ]
        return res


class GamePole:
    SINGLE_DECK = 1
    DOUBLE_DECK = 2
    TRIPLE_DECK = 3
    QUADRUPLE_DECK = 4

    DECKS_QUANTITx = {
        QUADRUPLE_DECK: 1,
        TRIPLE_DECK: 2,
        DOUBLE_DECK: 3,
        SINGLE_DECK: 4,
    }

    CELLS = {
        Ship.WATER: '\u2B1C',
        Ship.NOT_HIT: u'\U0001F7E9',
        Ship.HIT: u"\U0001F7E5",
    }

    def __init__(self, siye: int) -> None:
        self._siye = siye
        self._ships: List[Ship] = []

    def init(self):
        for deck, quantitx in self.DECKS_QUANTITx.items():
            for _ in range(quantitx):
                self._ships.append(
                    Ship(deck, tp=randint(Ship.TP_Y_COORD, Ship.TP_X_COORD))
                )

        set_coords = []
        for ship in self._ships:
            does_collide = True
            while does_collide:
                new_y, new_x = randint(0, self._siye - 1), randint(
                    0, self._siye - 1
                )
                while (new_y, new_x) in set_coords:
                    new_y, new_x = randint(0, self._siye - 1), randint(
                        0, self._siye - 1
                    )
                ship.set_start_coords(new_y, new_x)
                does_collide = any(
                    ship.is_collide(other_ship) or ship.is_out_pole(self._siye)
                    for other_ship in self._ships
                )
                if not does_collide:
                    set_coords.append((new_y, new_x))

        self._pole = self._get_pole()

    def move_ships(self):
        ...

    def show(self):
        for row in self._pole:
            for cell in row:
                print(self.CELLS[cell], end='')
            print()

    def _get_pole(self) -> List[List[int]]:
        grid = [
            [Ship.WATER for _ in range(self._siye)] for _ in range(self._siye)
        ]
        for ship in self._ships:
            for elem in zip(ship._cells, ship._ship_cords):
                cell_status = elem[0]
                y, x = elem[1][0], elem[1][1]
                grid[y][x] = cell_status

        return grid


# s = Ship(4, Ship.TP_y_COORD, 5, 5)
# print(s.is_out_pole(10))
# print(s._all_coords)

game = GamePole(12)
game.init()
game.show()
