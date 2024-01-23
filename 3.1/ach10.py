import time
from typing import Any


class Filter:
    def __init__(self, date: float) -> None:
        self.date = date

    def __setattr__(self, __name: str, __value: Any) -> None:
        if getattr(self, __name, None) is None:
            super().__setattr__(__name, __value)


class Mechanical(Filter):
    ...


class Aragon(Filter):
    ...


class Calcium(Filter):
    ...


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self) -> None:
        self.slots = [0] * 3

    def add_filter(self, slot_num: int, filter: Filter) -> None:
        if slot_num == 1 and type(filter) is Mechanical:
            self.slots[0] = filter
        elif slot_num == 2 and type(filter) is Aragon:
            self.slots[1] = filter
        elif slot_num == 3 and type(filter) is Calcium:
            self.slots[2] = filter

    def remove_filter(self, slot_num: int) -> None:
        self.slots[slot_num - 1] = 0

    def get_filters(self) -> tuple[Filter]:
        return tuple(self.slots)

    def water_on(self) -> bool:
        return all(self.slots) and all(
            0 <= time.time() - filter.date <= self.MAX_DATE_FILTER
            for filter in self.slots
        )


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
print(w)
