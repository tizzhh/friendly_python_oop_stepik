from abc import ABC, abstractmethod
from typing import Any, Union


class StackObj:
    def __init__(self, data: Any) -> None:
        self._data = data
        self._next = None


class StackInterface(ABC):
    @abstractmethod
    def push_back(self, obj: StackObj) -> None:
        ...

    @abstractmethod
    def pop_back(self) -> Union[None, StackObj]:
        ...


class Stack(StackInterface):
    def __init__(self) -> None:
        self._top: StackObj = None

    def push_back(self, obj: StackObj) -> None:
        if self._top is None:
            self._top = obj
        else:
            ptr = self._top
            while ptr._next is not None:
                ptr = ptr._next
            ptr._next = obj

    def pop_back(self) -> Union[None, StackObj]:
        if self._top is None:
            return None
        prev = ptr = self._top
        while ptr._next is not None:
            prev = ptr
            ptr = ptr._next
        if ptr == self._top:
            self._top = None
        prev._next = None
        return ptr


assert issubclass(
    Stack, StackInterface
), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert (
        False
    ), "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1
assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"
