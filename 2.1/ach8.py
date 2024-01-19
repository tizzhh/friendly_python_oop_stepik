class Point:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, *args) -> None:
        if len(args) == 2:
            self.set_coords(*args)
        elif len(args) == 4:
            self.__sp, self.__ep = Point(*args[:2]), Point(*args[2:])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        print(
            f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}'
        )


rect = Rectangle(0, 0, 20, 34)
rect.draw()
