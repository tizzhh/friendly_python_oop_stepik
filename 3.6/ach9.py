from typing import Any, Union


class Dimensions:
    def __init__(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self) -> int:
        return hash(tuple(self.__dict__.values()))

    def __setattr__(self, __name: str, __value: Any) -> None:
        try:
            val = float(__value)
        except ValueError:
            ...
        if val <= 0:
            raise ValueError(
                "габаритные размеры должны быть положительными числами"
            )
        super().__setattr__(__name, __value)

    def __repr__(self) -> str:
        return f'Dimensions obj {self.a} {self.b} {self.c}'


s_inp = input()
lst_dims = [Dimensions(*data.split()) for data in s_inp.split('; ')]
lst_dims.sort(key=lambda x: hash(x))
print(lst_dims)
