from typing import Any, Union


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self) -> Union[int, float]:
        return super().__getattribute__('__a')

    @a.setter
    def a(self, a: Union[int, float]) -> None:
        super().__setattr__('__a', a)

    @property
    def b(self) -> Union[int, float]:
        return super().__getattribute__('__b')

    @b.setter
    def b(self, b: Union[int, float]) -> None:
        super().__setattr__('__b', b)

    @property
    def c(self) -> Union[int, float]:
        return super().__getattribute__('__c')

    @c.setter
    def c(self, c: Union[int, float]) -> None:
        super().__setattr__('__c', c)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['MIN_DIMENSION', 'MAX_DIMENSION']:
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )
        elif __name in ['a', 'b', 'c']:
            if self.MIN_DIMENSION <= __value <= self.MAX_DIMENSION:
                super().__setattr__(__name, __value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
print(d.__dict__)
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
