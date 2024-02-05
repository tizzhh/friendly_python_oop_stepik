class Vector:
    def __init__(self, *args) -> None:
        self.coords = list(args)

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        return self._do_oper(other, lambda x: x[0] + x[1])

    def __sub__(self, other):
        return self._do_oper(other, lambda x: x[0] - x[1])

    def _do_oper(self, other, func):
        if len(self) != len(other):
            raise TypeError('размерности векторов не совпадают')
        new_data = [func(elem) for elem in zip(self.coords, other.coords)]
        if all(isinstance(x, int) for x in other.coords):
            return VectorInt(*new_data)
        return Vector(*new_data)

    def get_coords(self):
        return tuple(self.coords)


class VectorInt(Vector):
    def __init__(self, *args) -> None:
        if not all(isinstance(x, int) for x in args):
            raise ValueError('координаты должны быть целыми числами')
        super().__init__(*args)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)
v3 = v1 + v2
print(v3)
assert (v1 + v2).get_coords() == (
    4,
    6,
    8,
), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (
    -2,
    -2,
    -2,
), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(
    v, Vector
), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"


v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert (
    type(v) == VectorInt
), "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
assert (
    type(v) == Vector
), "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
