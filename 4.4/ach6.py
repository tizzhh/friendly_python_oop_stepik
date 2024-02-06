class Furniture:
    def __init__(self, name, weight) -> None:
        self._name = name
        self._weight = weight

    def __setattr__(self, atr, __value) -> None:
        if atr == '_name':
            self.__verify_name(__value)
        elif atr == '_weight':
            self.__verify_weight(__value)
        super().__setattr__(atr, __value)

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        return name

    def __verify_weight(self, weight):
        if not isinstance(weight, (int, float)) or not weight > 0:
            raise TypeError('вес должен быть положительным числом')
        return weight

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors) -> None:
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height) -> None:
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square) -> None:
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
# tb = Table('стол', 34.5, 75, 10)
# print(tb.get_attrs())
