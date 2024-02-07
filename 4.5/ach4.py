from itertools import count


class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    _id = count(0)

    def __init__(self, name, weight, price) -> None:
        self.__id = next(self._id)
        self._name = name
        self._weight = weight
        self._price = price

    def get_id(self):
        return self.__id


a = ShopItem('a', 1, 2)
b = ShopItem('a', 1, 2)
print(a.__dict__, b.__dict__)
