from typing import Callable, Union


def check_indx(func: Callable) -> Callable:
    def wrapper(self, *args, **kwargs) -> Union[int, None]:
        indx = args[0]
        if isinstance(indx, int) and not 0 <= indx < len(self.coords):
            raise IndexError('неверный индекс клетки')
        return func(self, *args, **kwargs)

    return wrapper


class RadiusVector:
    def __init__(self, *args: Union[int, float]) -> None:
        self.coords = list(args)

    @check_indx
    def __getitem__(self, indx: slice) -> Union[int, float]:
        return tuple(self.coords)[indx]

    def __setitem__(self, indx: slice, value: Union[int, float]) -> None:
        self.coords[indx] = value

    def __str__(self) -> str:
        return ' '.join(map(str, self.coords))


v = RadiusVector(1, 1, 1, 1)
print(v[1])  # 1
v[:] = 1, 2, 3, 4
print(v)  # 1
print(v[2])  # 3
print(v[1:])  # (2, 3, 4)
v[0] = 10.5
