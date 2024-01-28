from typing import Any, Union


class TriangleDesc:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, val):
        if not isinstance(val, (int, float)) or val <= 0:
            raise ValueError(
                "длины сторон треугольника должны быть положительными числами"
            )
        setattr(instance, self.name, val)
        if len(instance.__dict__.values()) == 3:
            self.__check_is_triangle(instance)

    @staticmethod
    def __check_is_triangle(instance) -> None:
        a, b, c = instance.a, instance.b, instance.c
        if not (a < b + c and b < a + c and c < a + b):
            raise ValueError(
                "с указанными длинами нельзя образовать треугольник"
            )


class Triangle:
    a = TriangleDesc()
    b = TriangleDesc()
    c = TriangleDesc()

    def __init__(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.__check_is_triangle()

    def __len__(self) -> int:
        return int(sum(self.__dict__.values()))

    def __call__(self, *args: Any, **kwds: Any) -> float:
        p = sum(self.__dict__.values()) / 2
        a, b, c = self.a, self.b, self.c
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    def __check_is_triangle(self) -> None:
        a, b, c = self.a, self.b, self.c
        if not a < b + c and b < a + c and c < a + b:
            raise ValueError(
                "с указанными длинами нельзя образовать треугольник"
            )
