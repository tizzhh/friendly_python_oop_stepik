from typing import Any


class Product:
    __product_id = 1

    def __init__(self, name: str, weight: int, price: int) -> None:
        self.id = self.product_id
        self.name = name
        self.weight = weight
        self.price = price
        self.id_increase()

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['id', 'weight', 'price']:
            if not isinstance(__value, int) or __value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        if __name == 'name':
            if not isinstance(__value, str):
                raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(__name, __value)

    def __delattr__(self, __name: str) -> None:
        if __name == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        super().__delattr__(__name)

    @classmethod
    def id_increase(cls) -> None:
        cls.__product_id += 1


class Shop:
    def __init__(self, name: str) -> None:
        self.name = name
        self.goods: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
