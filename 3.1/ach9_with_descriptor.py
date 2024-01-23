from typing import Any, Union


class DimensionsDecr:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, val):
        if instance.MIN_DIMENSION <= val <= instance.MAX_DIMENSION:
            setattr(instance, self.name, val)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    a = DimensionsDecr()
    b = DimensionsDecr()
    c = DimensionsDecr()

    def __init__(
        self, a: Union[int, float], b: Union[int, float], c: Union[int, float]
    ) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['MIN_DIMENSION', 'MAX_DIMENSION']:
            raise AttributeError(
                "Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено."
            )
        super().__setattr__(__name, __value)


d = Dimensions(10.5, 20.1, 30)
d.a = 8
d.b = 15
# print(d.__dict__)
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# d.MAX_DIMENSION = 10  # исключение AttributeError
