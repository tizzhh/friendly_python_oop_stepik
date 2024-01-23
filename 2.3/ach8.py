class DescriptorBase:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.check_val(value):
            setattr(instance, self.name, value)


class PriceValue(DescriptorBase):
    MIN_VALUE = 0

    def __init__(self, max_value=0) -> None:
        self.max_value = max_value

    def check_val(self, price):
        return (
            isinstance(price, (int, float))
            and self.MIN_VALUE <= price <= self.max_value
        )


class StringValue(DescriptorBase):
    def __init__(self, min_length=0, max_length=0) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def check_val(self, name):
        return (
            isinstance(name, str)
            and self.min_length <= len(name) <= self.max_length
        )


class Product:
    MIN_LENGTH = 2
    MAX_LENGTH = 50
    MAX_VALUE = 10000
    name = StringValue(MIN_LENGTH, MAX_LENGTH)
    price = PriceValue(MAX_VALUE)

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name) -> None:
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")
