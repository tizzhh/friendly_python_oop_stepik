import operator as op
from typing import Callable, List, Union


class Vector:
    def __init__(self, *args) -> None:
        self.coords: List[Union[int, float]] = list(args)

    def __add__(self, other: 'Vector') -> 'Vector':
        return self.__do_calc(op.add, other)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return self.__do_calc(op.sub, other)

    def __mul__(self, other: 'Vector') -> 'Vector':
        return self.__do_calc(op.mul, other)

    def __iadd__(self, other: Union[int, float, 'Vector']) -> 'Vector':
        return self.__do_calc(op.add, other, False)

    def __isub__(self, other: Union[int, float, 'Vector']) -> 'Vector':
        return self.__do_calc(op.sub, other, False)

    def __str__(self) -> str:
        return ' '.join(map(str, self.coords))

    def __eq__(self, other: 'Vector') -> bool:
        for x, y in zip(self.coords, other.coords):
            if x != y:
                return False
        return True

    def __len__(self) -> int:
        return len(self.coords)

    def __do_calc(
        self,
        func: Callable,
        other: Union[int, float, 'Vector'],
        new_obj: bool = True,
    ):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            new_coords = [
                func(x, y) for x, y in zip(self.coords, other.coords)
            ]
            if new_obj:
                return self.__class__(*new_coords)
            self.coords = new_coords
            return self
        elif isinstance(other, (int, float)):
            self.coords = [func(x, other) for x in self.coords]
            return self
