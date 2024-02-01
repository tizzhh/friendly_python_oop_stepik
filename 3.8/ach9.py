from typing import Callable, List, Union


def check_indx(func: Callable):
    def wrapper(self, *args, **kwargs) -> Union[None, Thing]:
        indx = args[0]
        if not 0 <= indx < len(self.bag):
            raise IndexError('неверный индекс')
        return func(self, *args, **kwargs)

    return wrapper


class Thing:
    def __init__(self, name: str, weight: Union[int, float]) -> None:
        self.name = name
        self.weight = weight


class Bag:
    @staticmethod
    def check_indx(func: Callable):
        def wrapper(self, *args, **kwargs) -> Union[None, Thing]:
            indx = args[0]
            if not 0 <= indx < len(self.bag):
                raise IndexError('неверный индекс')
            return func(self, *args, **kwargs)

        return wrapper

    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.bag: List[Thing] = []
        self._cur_weight = 0

    def add_thing(self, thing: Thing) -> None:
        if self._cur_weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag.append(thing)
        self._cur_weight += thing.weight

    @check_indx
    def __getitem__(self, indx: int) -> Thing:
        return self.bag[indx]

    @check_indx
    def __setitem__(self, indx: int, thing: Thing) -> None:
        prev_thing = self.bag[indx]
        if (
            self._cur_weight - prev_thing.weight + thing.weight
            > self.max_weight
        ):
            raise ValueError('превышен суммарный вес предметов')
        self.bag[indx] = thing
        self._cur_weight = self._cur_weight - prev_thing.weight + thing.weight

    @check_indx
    def __delitem__(self, indx: int) -> None:
        del self.bag[indx]


# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# print(bag[2].name)  # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name)  # платок
# del bag[0]
# print(bag[0].name)  # платок
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert (
    b[0].name == 'книга' and b[0].weight == 100
), "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert (
    b[1].name == 'Python' and b[1].weight == 20
), "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert (
    b[0].name == 'Python' and b[0].weight == 20
), "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"
