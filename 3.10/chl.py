from random import choice
from typing import Callable, List, Tuple, Union


class Cell:
    def __init__(self) -> None:
        self.value = 0

    def __bool__(self) -> bool:
        return self.value == 0


class TicTacToe:
    WIDTH = 3
    HEIGHT = 3
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    DISPLAY_DATA = {
        0: u'\u2b1c',
        1: u'\u274c',
        2: u'\u2b55',
    }

    def check_indx(func: Callable) -> Callable:
        def wrapper(self: 'TicTacToe', *args, **kwargs) -> Union[int, None]:
            indexes = args[0]
            if not all(isinstance(indx, int) for indx in indexes) or not all(
                0 <= indx < self.HEIGHT for indx in indexes
            ):
                raise IndexError('некорректно указанные индексы')
            return func(self, *args, **kwargs)

        return wrapper

    def __init__(self) -> None:
        self.pole: List[List[Cell]] = [
            [Cell() for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)
        ]
        self.__game_is_finished = False

    @check_indx
    def __getitem__(self, indx: Tuple[int]) -> int:
        x, y = indx[0], indx[1]
        return self.pole[x][y].value

    @check_indx
    def __setitem__(self, indx: Tuple[int], value: int) -> None:
        x, y = indx[0], indx[1]
        self.pole[x][y].value = value

    def __bool__(self) -> bool:
        if self.__game_is_finished:
            return False
        for row in self.pole:
            for cell in row:
                if cell:
                    return True
        return False

    def init(self) -> None:
        for row in self.pole:
            for cell in row:
                cell.value = self.FREE_CELL

    def show(self) -> None:
        for row in self.pole:
            for cell in row:
                print(self.DISPLAY_DATA[cell.value], end=' ')
            print()
        print()

    def human_go(self) -> None:
        x, y = self.__get_human_coords()
        while not self.pole[x][y]:
            print('Cell is already occupied!')
            x, y = self.__get_human_coords()
        self.pole[x][y].value = self.HUMAN_X

    @staticmethod
    def __get_human_coords() -> Tuple[int]:
        try:
            inp = map(int, input("Input your coordinates: ").strip().split())
        except ValueError:
            raise ValueError('Coordinates should be integers!')

        try:
            x, y = inp
        except ValueError:
            raise ValueError('There should be two cooridinates!')
        return (x, y)

    def computer_go(self) -> None:
        choice(
            [
                cell
                for row in self.pole
                for cell in row
                if cell.value == self.FREE_CELL
            ]
        ).value = self.COMPUTER_O

    @property
    def is_human_win(self) -> bool:
        return self.__check_who_wins(self.HUMAN_X)

    @property
    def is_computer_win(self) -> bool:
        return self.__check_who_wins(self.COMPUTER_O)

    @property
    def is_draw(self) -> bool:
        return not self and not self.is_computer_win and not self.is_human_win

    def __check_who_wins(self, type_of_player: int) -> bool:
        win_condition = [type_of_player for _ in range(self.HEIGHT)]
        pole_of_vals = [[cell.value for cell in row] for row in self.pole]

        self.__game_is_finished = True
        if any(row == win_condition for row in pole_of_vals):
            return True

        pole_of_vals = [list(tpl) for tpl in zip(*pole_of_vals)]
        if any(row == win_condition for row in pole_of_vals):
            return True

        if all(pole_of_vals[i][i] == type_of_player for i in range(3)):
            return True

        if all(
            pole_of_vals[i][self.WIDTH - 1 - i] == type_of_player
            for i in range(3)
        ):
            return True

        self.__game_is_finished = False
        return False


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game[0, 1] = 1
game[1, 1] = 1
game[2, 1] = 1
game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")
