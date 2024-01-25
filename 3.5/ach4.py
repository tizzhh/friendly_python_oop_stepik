from typing import Self, Union


class DimDescr:
    def __set_name__(self, owner: 'Dimensions', name: str) -> None:
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance: 'Dimensions', owner: 'Dimensions') -> int:
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance: 'Dimensions', value: int) -> None:
        if instance.MIN_DIMENSION <= value <= instance.MAX_DIMENSION:
            setattr(instance, self.name, value)


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    a = DimDescr()
    b = DimDescr()
    c = DimDescr()

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__a = 0
        obj.__b = 0
        obj.__c = 0
        return obj

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __lt__(self, other: Self) -> bool:
        return self.volume() < other.volume()

    def __le__(self, other: Self) -> bool:
        return self.volume() <= other.volume()

    def volume(self) -> float:
        return self.a * self.b * self.c


class ShopItem:
    def __init__(
        self, name: str, price: Union[int, float], dim: Dimensions
    ) -> None:
        self.name = name
        self.price = price
        self.dim = dim


trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
lst_shop = (trainers, umbrella, fridge, chair)
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim.volume())
print(lst_shop_sorted)
assert len(lst_shop) == 4, "число элементов в lst_shop не равно 4"

lst_sp = []
lst_sp.append(ShopItem('кеды', 1024, Dimensions(40, 30, 120)))
lst_sp.append(ShopItem('зонт', 500.24, Dimensions(10, 20, 50)))
lst_sp.append(ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)))
lst_sp.append(ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200)))

lst_sp_sorted = ['зонт', 'кеды', 'табуретка', 'холодильник']
s = [x.name for x in lst_shop_sorted]
assert lst_sp_sorted == s, "список lst_shop_sorted сформирован неверно"

d1 = Dimensions(40, 30, 120)
d2 = Dimensions(40, 30, 120)
d3 = Dimensions(30, 20, 100)
assert d1 <= d2, "неверно отработал оператор <="
assert d3 <= d2, "неверно отработал оператор <="
assert d3 < d2, "неверно отработал оператор <"

d2.a = 10
d2.b = 10
d2.c = 10
assert (
    d2 < d1
), "неверно отработал оператор < после изменения объема через объекты-свойства a, b, c"
