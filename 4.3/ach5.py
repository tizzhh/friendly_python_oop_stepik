from typing import List


class SellItem:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square) -> None:
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms) -> None:
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square) -> None:
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name) -> None:
        self.name = name
        self.__for_sale: List[SellItem] = []

    @property
    def for_sale(self) -> List[SellItem]:
        return self.__for_sale

    def add_object(self, obj: SellItem) -> None:
        self.for_sale.append(obj)

    def remove_object(self, obj) -> None:
        self.for_sale.remove(obj)

    def get_objects(self) -> List[SellItem]:
        return self.for_sale
