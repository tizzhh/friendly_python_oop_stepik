from math import sqrt
from typing import Union


class Complex:
    def __init__(
        self, real: Union[int, float], img: Union[int, float]
    ) -> None:
        self.real = real
        self.img = img

    def __abs__(self) -> float:
        real, img = self.real, self.img
        return sqrt(real * real + img * img)

    @property
    def real(self) -> Union[int, float]:
        return self.__real

    @real.setter
    def real(self, real: Union[int, float]) -> None:
        if not isinstance(real, (int, float)):
            raise ValueError("Неверный тип данных.")
        self.__real = real

    @property
    def img(self) -> Union[int, float]:
        return self.__img

    @img.setter
    def img(self, img: Union[int, float]) -> None:
        if not isinstance(img, (int, float)):
            raise ValueError("Неверный тип данных.")
        self.__img = img


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
print(c_abs)
