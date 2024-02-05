class Thing:
    def __init__(self, name, price, weight) -> None:
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self) -> int:
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, thing={}):
        if not isinstance(thing, dict):
            raise TypeError('аргумент должен быть словарем')
        self._check_keys(thing)
        return super().__init__(thing)

    def __setitem__(self, indx, val):
        self._check_keys((indx,))
        return super().__setitem__(indx, val)

    @staticmethod
    def _check_keys(thing):
        for key in thing:
            if not isinstance(key, Thing):
                raise TypeError(
                    'ключами могут быть только объекты класса Thing'
                )


th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2

for x in dict_things:
    print(x.name)
