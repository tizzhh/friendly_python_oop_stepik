class Digit:
    def __init__(self, val) -> None:
        if not isinstance(val, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.val = val


class Integer(Digit):
    def __init__(self, val) -> None:
        if not isinstance(val, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(val)


class Float(Digit):
    def __init__(self, val) -> None:
        if not isinstance(val, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(val)


class Positive(Digit):
    def __init__(self, val) -> None:
        if not isinstance(val, (int, float)) or not val > 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(val)


class Negative(Digit):
    def __init__(self, val) -> None:
        if not isinstance(val, (int, float)) or not val < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(val)


class PrimeNumber(Integer, Positive):
    ...


class FloatPositive(Float, Positive):
    ...


digits = [
    PrimeNumber(3),
    PrimeNumber(1),
    PrimeNumber(4),
    FloatPositive(1.5),
    FloatPositive(9.2),
    FloatPositive(6.5),
    FloatPositive(3.5),
    FloatPositive(8.9),
]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))


print(lst_positive, lst_float)
