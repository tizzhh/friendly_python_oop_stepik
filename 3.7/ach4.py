import sys


class Player:
    def __init__(self, name: str, old: int, score: int) -> None:
        self.name = name
        self.old = old
        self.score = int(score)

    def __bool__(self) -> bool:
        return self.score > 0


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = [Player(*string.split('; ')) for string in lst_in]
players_filtered = list(filter(None, players))
print(players_filtered)
