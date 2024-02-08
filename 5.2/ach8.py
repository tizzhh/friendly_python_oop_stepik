class Rect:
    def __init__(self, x, y, width, height) -> None:
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._check_args(*self.__dict__.values())

    @staticmethod
    def _check_args(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError(
                    'некорректные координаты и параметры прямоугольника'
                )
        for arg in args[2:]:
            if not arg > 0:
                raise ValueError(
                    'некорректные координаты и параметры прямоугольника'
                )

    def is_collision(self, rect: 'Rect'):
        if (
            not self._x + self._width < rect._x
            and not self._x > rect._x + rect._width
            and not self._y < rect._y - rect._height
            and not self._y - self._height > rect._y
        ):
            raise TypeError('прямоугольники пересекаются')


lst_rect = [
    Rect(0, 0, 5, 3),
    Rect(6, 0, 3, 5),
    Rect(3, 2, 4, 4),
    Rect(0, 8, 8, 1),
]
lst_not_collision = []
for rect in lst_rect:
    collision = False
    for rect2 in lst_rect:
        if rect == rect2:
            continue
        try:
            rect.is_collision(rect2)
        except:
            collision = True
            break
    if not collision:
        lst_not_collision.append(rect)


print(lst_not_collision)
