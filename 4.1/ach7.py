class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Game(Singleton):
    def __init__(self, name) -> None:
        if 'name' not in self.__dict__:
            self.name = name


game = Game('aboba')
game2 = Game('aboba2')
print(game.name, game2.name)
