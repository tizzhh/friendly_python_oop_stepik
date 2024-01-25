from typing import Union

from typing_extensions import Self


class StackObj:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str) -> None:
        self.__data = data

    @property
    def next(self) -> Self:
        return self.__next

    @next.setter
    def next(self, next) -> None:
        self.__next = next


class Stack:
    def __init__(self) -> None:
        self.top = None

    def __str__(self) -> str:
        res = ''
        pointer = self.top
        res += pointer.data
        while pointer.next is not None:
            pointer = pointer.next
            res += ', ' + pointer.data
        return res

    def __add__(self, other: StackObj) -> Self:
        return self.add_mul_opers(other)

    def __iadd__(self, other: StackObj) -> Self:
        return self.add_mul_opers(other)

    def __mul__(self, other: list) -> Self:
        return self.add_mul_opers(other, True)

    def __imul__(self, other: list) -> Self:
        return self.add_mul_opers(other, True)

    def add_mul_opers(self, other: Union[StackObj, list], mul: bool = False):
        if not mul:
            if not isinstance(other, StackObj):
                raise TypeError('Only StackObj can be pushed to the stack')
            self.push_back(other)
        else:
            if not isinstance(other, list) or isinstance(other[0], StackObj):
                raise TypeError('Mult only supports lists of data')
            for elem in other:
                self.push_back(StackObj(elem))
        return self

    def push_back(self, obj: StackObj) -> None:
        if self.top is None:
            self.top = obj
        else:
            pointer = self.top
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = obj

    def pop_back(self) -> None:
        if self.top is None:
            return
        pointer = self.top
        prev = None
        while pointer.next is not None:
            prev = pointer
            pointer = pointer.next
        prev.next = None

    @property
    def top(self) -> StackObj:
        return self.__top

    @top.setter
    def top(self, obj) -> None:
        self.__top = obj


st = Stack()
st.push_back(StackObj('aboba'))
st.push_back(StackObj('aboba2'))
st.push_back(StackObj('aboba3'))
st.pop_back()
print(st)

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert (
        h._StackObj__data == d[i]
    ), "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
