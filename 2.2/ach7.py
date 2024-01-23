class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0) -> None:
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y

    @classmethod
    def __check_coords(cls, coord):
        return (
            isinstance(coord, (int, float))
            and cls.MIN_COORD <= coord <= cls.MAX_COORD
        )

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x if self.__check_coords(x) else self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y if self.__check_coords(y) else self.__y

    @staticmethod
    def norm2(vector):
        x, y = vector.x, vector.y
        return x * x + y * y


# aboba = RadiusVector2D(2, 3)
# print(aboba.x, aboba.y)
# aboba.x = 7
# print(aboba.x, aboba.y)
r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)
# print(r3.__dict__)
assert hasattr(RadiusVector2D, 'MIN_COORD') and hasattr(
    RadiusVector2D, 'MAX_COORD'
), "в классе RadiusVector2D должны присутствовать атрибуты MIN_COORD и MAX_COORD"

assert (
    type(RadiusVector2D.x) == property and type(RadiusVector2D.y) == property
), "в классе RadiusVector2D должны присутствовать объекты-свойства x и y"

assert (
    r1.x == 0
    and r1.y == 0
    and r2.x == 1
    and r2.y == 0
    and r3.x == 4
    and r3.y == 5
), "свойства x и y возвращают неверные значения"

assert RadiusVector2D.norm2(r3) == 41, "неверно вычисляется норма вектора"

r4 = RadiusVector2D(4.5, 5.5)
assert (
    4.4 < r4.x < 4.6 and 5.4 < r4.y < 5.6
), "свойства x и y возвращают неверные значения"

r5 = RadiusVector2D(-102, 2000)
assert (
    r5.x == 0 and r5.y == 0
), "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"

r = RadiusVector2D(10, 20)
r.x = 'a'
r.y = (1, 2)
print(r.x, r.y)
assert (
    r.x == 10 and r.y == 20
), "присвоение не числовых значений должно игнорироваться"
