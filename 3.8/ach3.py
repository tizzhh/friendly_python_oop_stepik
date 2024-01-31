from typing import Callable, Tuple, Union


def check_indx(func: Callable):
    def wrapper(self, *args, **kwargs):
        if (
            not isinstance(args[0], int)
            or not 0 <= args[0] <= len(self.coords) - 2
        ):
            raise IndexError('некорректный индекс')
        return func(self, *args, **kwargs)

    return wrapper


class Track:
    def __init__(
        self, start_x: Union[int, float], start_y: Union[int, float]
    ) -> None:
        self.coords = [] + [[(start_x, start_y), 0]]

    def add_point(
        self,
        x: Union[int, float],
        y: Union[int, float],
        speed: Union[int, float],
    ) -> None:
        self.coords.append([(x, y), speed])

    @check_indx
    def __getitem__(self, indx: int) -> Tuple[Tuple[Union[int, float]]]:
        elem = self.coords[indx + 1]
        return elem[0], elem[1]

    @check_indx
    def __setitem__(self, indx: int, new_speed: Union[int, float]) -> None:
        self.coords[indx + 1][1] = new_speed


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)
