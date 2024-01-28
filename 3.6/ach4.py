from typing import Union


class Rect:
    def __init__(
        self,
        x: Union[int, float],
        y: Union[int, float],
        width: Union[int, float],
        height: Union[int, float],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __hash__(self) -> int:
        return hash((self.width, self.height))


r1 = Rect(10, 5, 100, 50)
r2 = Rect(-10, 4, 100, 50)

h1, h2 = hash(r1), hash(r2)
print(h1, h2)
