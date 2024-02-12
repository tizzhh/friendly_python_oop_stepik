from random import choice, randint
from typing import Callable, List, Set, Tuple


class Ship:
    WATER = 0
    NOT_HIT = 1
    HIT = 2

    TP_X_COORD = 1
    TP_Y_COORD = 2

    def __init__(
        self, length: int, tp: int = TP_X_COORD, x: int = None, y: int = None
    ) -> None:
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [self.NOT_HIT for _ in range(length)]
        self._ship_cords = self._get_ship_coords()
        self._all_coords = self._get_all_coords()

    @staticmethod
    def _get_set_items_check_args(func: Callable) -> Callable:
        def wrapper(self: 'Ship', *args, **kwargs):
            indy = args[0]
            if not isinstance(indy, int):
                raise TypeError('Index should be int')
            if not 0 <= abs(indy) < len(self._cells):
                raise IndexError('Index out or range')
            if len(args) == 2:
                val = args[1]
                if val not in [self.HIT, self.NOT_HIT]:
                    raise ValueError('Wrong value, should be 1 or 2')
            return func(self, *args, **kwargs)

        return wrapper

    @_get_set_items_check_args
    def __getitem__(self, indy: int):
        return self._cells[indy]

    @_get_set_items_check_args
    def __setitem__(self, indy: int, value: int):
        self._cells[indy] = value

    def __repr__(self) -> str:
        return f'coords: {self._x} {self._y}, length: {self._length}'

    def set_start_coords(self, x: int, y: int) -> None:
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError('Coords should be int')
        self._x = x
        self._y = y
        self._ship_cords = self._get_ship_coords()
        self._all_coords = self._get_all_coords()

    def get_start_coords(self) -> Tuple[int]:
        return (self._x, self._y)

    def move(self, go: int) -> None:
        if self._is_move:
            if self._tp == self.TP_X_COORD:
                self._x += go
            elif self._tp == self.TP_Y_COORD:
                self._y += go
        self._ship_cords = self._get_ship_coords()
        self._all_coords = self._get_all_coords()

    def is_collide(self, ship: 'Ship') -> bool:
        return self != ship and (
            bool(set(self._all_coords) & set(ship._ship_cords))
            or bool(set(self._ship_cords) & set(ship._all_coords))
        )

    def is_out_pole(self, size: int) -> bool:
        return not (
            0 <= self._x < size
            and 0 <= self._y < size
            and (
                0 <= self._x + self._length - 1 < size
                if self._tp == self.TP_X_COORD
                else 0 <= self._y + self._length - 1 < size
            )
        )

    def _get_all_coords(self) -> Set[Tuple[int]]:
        res = set()
        if self._x is not None and self._y is not None:
            for x, y in self._ship_cords:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        new_i, new_j = x + i, y + j
                        res.add((new_i, new_j))
        return res

    def _get_ship_coords(self) -> List[Tuple[int]]:
        res = []
        if self._x is not None and self._y is not None:
            res = [
                (self._x + step, self._y)
                if self._tp == self.TP_X_COORD
                else (self._x, self._y + step)
                for step in range(0, self._length)
            ]
        return res


class GamePole:
    SINGLE_DECK = 1
    DOUBLE_DECK = 2
    TRIPLE_DECK = 3
    QUADRUPLE_DECK = 4

    DECKS_QUANTITY = {
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

    def __init__(self, size: int) -> None:
        self._sixe = size
        self._ships: List[Ship] = []

    def init(self) -> None:
        for deck, quantity in self.DECKS_QUANTITY.items():
            for _ in range(quantity):
                self._ships.append(
                    Ship(deck, tp=choice([Ship.TP_X_COORD, Ship.TP_Y_COORD]))
                )

        set_coords = []
        for ship in self._ships:
            does_collide = True
            while does_collide:
                new_x, new_y = randint(0, self._sixe - 1), randint(
                    0, self._sixe - 1
                )
                while (new_x, new_y) in set_coords:
                    new_x, new_y = randint(0, self._sixe - 1), randint(
                        0, self._sixe - 1
                    )
                ship.set_start_coords(new_x, new_y)
                does_collide = any(
                    ship.is_collide(other_ship) or ship.is_out_pole(self._sixe)
                    for other_ship in self._ships
                )
                if not does_collide:
                    set_coords.append((new_x, new_y))

        self._pole = self._get_grid()

    def move_ships(self) -> None:
        for ship in self._ships:
            step = choice([-1, 1])
            ship.move(step)
            if any(
                ship.is_collide(other_ship) or ship.is_out_pole(self._sixe)
                for other_ship in self._ships
            ):
                ship.move(step)
                step = -step
                ship.move(step)
                if any(
                    ship.is_collide(other_ship) or ship.is_out_pole(self._sixe)
                    for other_ship in self._ships
                ):
                    ship.move(step)

        self._pole = self._get_grid()

    def show(self) -> None:
        for row in self._pole:
            for cell in row:
                print(self.CELLS[cell], end='')
            print()

    def _get_grid(self) -> List[List[int]]:
        grid = [
            [Ship.WATER for _ in range(self._sixe)] for _ in range(self._sixe)
        ]
        for ship in self._ships:
            for elem in zip(ship._cells, ship._ship_cords):
                cell_status = elem[0]
                x, y = elem[1][0], elem[1][1]
                grid[x][y] = cell_status

        return grid


# s = Ship(4, Ship.TP_X_COORD, 5, 5)
# print(s.is_out_pole(10))
# print(s._all_coords)

game = GamePole(10)
game.init()
# print(game._ships)
# game.show()
# game.move_ships()
# print()
# game.show()

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert (
    ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0
), "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert (
    ship._x == 1 and ship._y == 2
), "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (
    1,
    2,
), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)
# print(s1._all_coords, s3._all_coords, sep='\n')
assert s1.is_collide(
    s2
), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert (
    s1.is_collide(s3) == False
), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(
    s2
), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(
    10
), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert (
    s2.is_out_pole(10) == False
), "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"

p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert (
            s.is_out_pole(10) == False
        ), "корабли выходят за пределы игрового поля"

        for ship in p._ships:
            if s != ship:
                assert (
                    s.is_collide(ship) == False
                ), "корабли на игровом поле соприкасаются"
    p.move_ships()
