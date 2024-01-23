from typing import Union


class Thing:
    def __init__(self, name: str, weight: Union[int, float]) -> None:
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.__things = []

    def add_thing(self, thing: Thing):
        if self.check_weigth(thing.weight):
            self.things.append(thing)

    def remove_thing(self, indx: int):
        self.things.pop(indx)

    def get_total_weight(self) -> int:
        return sum([thing.weight for thing in self.things])

    @property
    def things(self) -> list[Thing]:
        return self.__things

    def check_weigth(self, weight):
        return self.get_total_weight() + weight <= self.max_weight


bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))
w = bag.get_total_weight()
print(w)
for t in bag.things:
    print(f"{t.name}: {t.weight}")
