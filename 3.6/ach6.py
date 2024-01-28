import sys
from typing import Union


class ShopItem:
    def __init__(
        self, name: str, weight: Union[int, float], price: Union[int, float]
    ) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other: 'ShopItem') -> bool:
        return self.__hash__() == other.__hash__()

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.weight, self.price))


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in2 = [
    [word for word in [s.split(': ')[0]] + s.split(': ')[-1].split()]
    for s in lst_in
]
lst_in2 = [ShopItem(*data) for data in lst_in2]
shop_items = {obj: [obj, lst_in2.count(obj)] for obj in lst_in2}
print(shop_items)
