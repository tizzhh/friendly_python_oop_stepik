from copy import deepcopy
from typing import Tuple, Union


class Box:
    def __init__(self, name: str, max_weight: Union[int, float]) -> None:
        self._name = name
        self._max_weight = max_weight
        self._things = []
        self._cur_weight = 0

    def add_thing(self, obj: Tuple[str, Union[int, float]]) -> None:
        if self._cur_weight + obj[1] > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')
        self._things.append(obj)
        self._cur_weight += obj[1]


class BoxDefender:
    def __init__(self, box: Box) -> None:
        self._box = box

    def __enter__(self) -> Box:
        self._copied_box = deepcopy(self._box)
        return self._copied_box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self._box.__dict__ = self._copied_box.__dict__


box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))
with BoxDefender(box) as b:
    b.add_thing(("зонт", 346.6))
    b.add_thing(("шина", 500))
    b.add_thing(("шина", 500))
print(box._things)
