from math import sqrt
from typing import Any, Union


class ComplexDescriptor:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner) -> Any:
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, value) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("Неверный тип данных.")
        setattr(instance, self.name, value)


class Complex:
    real = ComplexDescriptor()
    img = ComplexDescriptor()

    def __init__(
        self, real: Union[int, float], img: Union[int, float]
    ) -> None:
        self.real = real
        self.img = img

    def __abs__(self) -> float:
        real, img = self.real, self.img
        return sqrt(real * real + img * img)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)
