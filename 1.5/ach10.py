from random import randint


class Cell:
    def __init__(self, around_mines: int, mine: bool) -> None:
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M) -> None:
        self.N = N
        self.M = M
        self.pole = [
            [Cell(0, False) for _ in range(0, N)] for _ in range(0, N)
        ]
        self.init()

    def init(self):
        num_left = self.M
        while num_left:
            x, y = randint(0, self.N - 1), randint(0, self.N - 1)
            if not self.pole[x][y].mine:
                self.pole[x][y] = Cell(0, True)
                num_left -= 1
        self.set_around_mines()

    def set_around_mines(self):
        for i in range(0, self.N):
            for j in range(0, self.N):
                self.pole[i][j].around_mines = self.count_mines(i, j)

    def count_mines(self, i, j):
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                new_x, new_y = i + x, j + y
                if (
                    new_x < 0
                    or new_y < 0
                    or new_x >= self.N
                    or new_y >= self.N
                ):
                    continue
                if self.pole[new_x][new_y].mine:
                    count += 1

        if self.pole[i][j].mine:
            count -= 1
        return count

    def show(self):
        for i in self.pole:
            for j in i:
                if not j.fl_open:
                    print(j.around_mines if not j.mine else '*', end=' ')
                else:
                    print('#', end=' ')
            print('')


pole_game = GamePole(10, 12)
