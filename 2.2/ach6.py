class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @staticmethod
    def check_val(val):
        return isinstance(val, StackObj) or val is None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if self.check_val(obj):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class Stack:
    top: StackObj = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            pointer = self.top
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = obj

    def pop(self):
        pointer = self.top
        prev = None
        while pointer.next is not None:
            prev = pointer
            pointer = pointer.next
        if prev is not None:
            prev.next = None
        else:
            self.top = None
        return pointer

    def get_data(self):
        data = []
        pointer = self.top
        while pointer is not None:
            data.append(pointer.data)
            pointer = pointer.next
        return data


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()
res = s.get_data()
assert res == [
    "obj_1",
    "obj_2",
], f"метод get_data вернул неверные данные: {res}"
assert (
    s.top == top
), "атрибут top объекта класса Stack содержит неверное значение"
h = s.top
while h:
    res = h.data
    h = h.next
s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
print(s.get_data())
assert (
    s.get_data() == []
), f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert (
    n == 0
), "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"
s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"
