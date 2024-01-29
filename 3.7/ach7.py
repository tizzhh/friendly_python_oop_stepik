from typing import Tuple


class Ellipse:
    def __init__(self, *args) -> None:
        if len(args) == 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self) -> bool:
        return len(self.__dict__.values()) == 4

    def get_coords(self) -> Tuple[int]:
        if not self:
            raise AttributeError('нет координат для извлечения')
        return (self.x1, self.y1, self.x2, self.y2)


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for obj in lst_geom:
    if obj:
        obj.get_coords()
