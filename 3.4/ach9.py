from typing import Callable, Union

from typing_extensions import Self


class Box3D:
    def __init__(
        self,
        width: Union[int, float],
        height: Union[int, float],
        depth: Union[int, float],
    ) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other: Self) -> Self:
        return self.do_oper(
            self.__dict__.values(),
            other.__dict__.values(),
            lambda x: x[0] + x[1],
        )

    def __mul__(self, other: int) -> Self:
        return self.do_oper(
            self.__dict__.values(),
            [other] * len(self.__dict__),
            lambda x: x[0] * x[1],
        )

    def __rmul__(self, other: int) -> Self:
        return self * other

    def __sub__(self, other: Self) -> Self:
        return self.do_oper(
            self.__dict__.values(),
            other.__dict__.values(),
            lambda x: x[0] - x[1],
        )

    def __floordiv__(self, other: int) -> Self:
        return self.do_oper(
            self.__dict__.values(),
            [other] * len(self.__dict__),
            lambda x: x[0] // x[1],
        )

    def __mod__(self, other: int) -> Self:
        return self.do_oper(
            self.__dict__.values(),
            [other] * len(self.__dict__),
            lambda x: x[0] % x[1],
        )

    def do_oper(
        self, vals1: list[int], vals2: list[int], func: Callable
    ) -> Self:
        return self.__class__(*list(map(func, zip(vals1, vals2))))


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = (
    box1 + box2
)  # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = (
    box1 * 2
)  # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2  # Box3D: width=6, height=12, depth=18
box = (
    box2 - box1
)  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = (
    box1 // 2
)  # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3  # Box3D: width=2, height=1, depth=0
