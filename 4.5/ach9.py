class PointTrack:
    def __init__(self, x, y) -> None:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'PointTrack: {self.x}, {self.y}'


class Track:
    def __init__(self, *args) -> None:
        if len(args) == 2 and isinstance(args, int):
            self.__points = [PointTrack(args[0], args[1])]
        else:
            self.__points = [elem for elem in args]

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt: PointTrack):
        self.__points.append(pt)

    def add_front(self, pt: PointTrack):
        self.__points.insert(0, pt)

    def pop_back(self):
        self.__points.pop()

    def pop_front(self):
        self.__points.pop(0)


tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)
