from random import choice, randint
from typing import Callable, List, Set, Tuple

WHITE_SQUARE = '\u2B1C'
RED_SQUARE = u'\U0001F7E5'
GREEN_SQUARE = u'\U0001F7E9'
BLUE_SQUARE = u'\U0001F7E6'
BLACK_SQUARE = u"\u2B1B"


def generate_random_coorinates(size: int) -> Tuple[int]:
    return (randint(0, size - 1), randint(0, size - 1))


class Ship:
    WATER = 0
    NOT_HIT = 1
    HIT = 2

    TP_X_COORD = 1
    TP_Y_COORD = 2

    def __init__(
        self,
        length: int,
        tp: int = TP_X_COORD,
        x: int = None,
        y: int = None,
        hidden: bool = False,
    ) -> None:
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._hidden = hidden
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

    @property
    def ship_coords(self) -> List[Tuple[int]]:
        return self._ship_cords

    @property
    def cells(self) -> List[int]:
        return self._cells

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

    def __init__(self, size: int, color: str = GREEN_SQUARE) -> None:
        self._size = size
        self._ships: List[Ship] = []
        self.CELLS = {
            Ship.WATER: WHITE_SQUARE,
            Ship.NOT_HIT: color,
            Ship.HIT: RED_SQUARE,
        }
        self.CELLS[Ship.NOT_HIT] = color

    def __bool__(self) -> bool:
        return all(not ship._is_move for ship in self._ships)

    def is_game_over(self) -> bool:
        return bool(self)

    def init(self, hidden=False) -> None:
        for deck, quantity in self.DECKS_QUANTITY.items():
            for _ in range(quantity):
                self._ships.append(
                    Ship(
                        deck,
                        tp=choice([Ship.TP_X_COORD, Ship.TP_Y_COORD]),
                        hidden=hidden,
                    )
                )

        set_coords = []
        for ship in self._ships:
            does_collide = True
            while does_collide:
                new_x, new_y = generate_random_coorinates(self._size)
                while (new_x, new_y) in set_coords:
                    new_x, new_y = generate_random_coorinates(self._size)
                ship.set_start_coords(new_x, new_y)
                does_collide = any(
                    ship.is_collide(other_ship) or ship.is_out_pole(self._size)
                    for other_ship in self._ships
                )
                if not does_collide:
                    set_coords.append((new_x, new_y))

        self._pole = self._get_grid()

    @property
    def ships(self) -> List[Ship]:
        return self._ships

    def move_ships(self) -> None:
        for ship in self._ships:
            step = choice([-1, 1])
            ship.move(step)
            if any(
                ship.is_collide(other_ship) or ship.is_out_pole(self._size)
                for other_ship in self._ships
            ):
                ship.move(step)
                step = -step
                ship.move(step)
                if any(
                    ship.is_collide(other_ship) or ship.is_out_pole(self._size)
                    for other_ship in self._ships
                ):
                    ship.move(step)

        self._pole = self._get_grid()

    def show(self) -> None:
        self._pole = self._get_grid()
        for row in self._pole:
            for cell in row:
                print(self.CELLS[cell], end='')
            print()

    def _get_grid(self) -> List[List[int]]:
        grid = [
            [Ship.WATER for _ in range(self._size)] for _ in range(self._size)
        ]
        for ship in self._ships:
            for elem in zip(ship._cells, ship._ship_cords):
                cell_status = elem[0]
                x, y = elem[1][0], elem[1][1]
                grid[x][y] = cell_status if not ship._hidden else Ship.WATER

        return grid


class SeaBattle:
    def __init__(self, size: int) -> None:
        self.player = GamePole(size)
        self.enemy = GamePole(size, color=BLUE_SQUARE)
        self._size = size
        self.start()

    def __bool__(self) -> bool:
        return not self.player.is_game_over() and not self.enemy.is_game_over()

    def show(self) -> None:
        print("\033[H\033[J", end="")
        print('You:')
        self.player.show()
        print(BLACK_SQUARE * self._size)
        print('Enemy:')
        self.enemy.show()

    def move(self) -> None:
        self.player.move_ships()
        self.enemy.move_ships()

    def check_who_won(self) -> None:
        if self.player.is_game_over():
            print('Computer wins!')
        elif self.enemy.is_game_over():
            print('Player wins!')

    def start(self) -> None:
        self.player.init()
        self.enemy.init(hidden=True)

    def user_turn(self) -> None:
        inp = input('Input enemy coordinates: ').split()
        try:
            x, y = map(int, inp)
        except ValueError:
            raise ValueError('Coordinates should be int and only 2')
        coord = (x, y)
        for ship in self.enemy.ships:
            if coord in ship.ship_coords:
                ship.cells[ship.ship_coords.index(coord)] = Ship.HIT
                ship._is_move = False
                ship._hidden = False
                print('Hit!')
                return
        print("You've missed!")

    def computer_turn(self) -> None:
        coord = generate_random_coorinates(self.enemy._size)
        for ship in self.player.ships:
            if coord in ship.ship_coords:
                ship.cells[ship.ship_coords.index(coord)] = Ship.HIT
                return
        print("Computer missed")


battleship = SeaBattle(10)
while battleship:
    battleship.show()
    battleship.user_turn()
    battleship.computer_turn()
    battleship.move()
    battleship.show()

battleship.check_who_won()
