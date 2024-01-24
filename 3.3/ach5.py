class ObjListDescriptor:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, val):
        setattr(instance, self.name, val)


class ObjList:
    data = ObjListDescriptor()
    prev = ObjListDescriptor()
    next = ObjListDescriptor()

    def __init__(self, data: str) -> None:
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return f'Obj: {self.data} prev: {self.prev.data if self.prev else None}, next: {self.next.data if self.next else None}'


class LinkedList:
    def __init__(self) -> None:
        self.head: ObjList = None
        self.tail: ObjList = None

    def add_obj(self, obj: ObjList) -> None:
        if self.head is None:
            self.tail = self.head = obj
        else:
            prev_tail = self.tail
            self.tail.next = obj
            self.tail = obj
            self.tail.prev = prev_tail

    def remove_obj(self, indx: int) -> None:
        if indx < len(self) and indx >= 0:
            if self.head is self.tail:
                self.head = self.tail = None
            elif indx == 0:
                if self.head is not None:
                    self.head = self.head.next
                    if self.head is not None:
                        self.head.prev = None
            elif indx == len(self) - 1:
                if self.tail is not None:
                    self.tail = self.tail.prev
                    if self.tail is not None:
                        self.tail.next = None
            else:
                counter = 0
                pointer = self.head
                while counter < indx and pointer.next is not None:
                    pointer = pointer.next
                temp = pointer
                temp = temp.prev
                temp.next = pointer.next
                pointer.prev = None

    def __call__(self, indx: int) -> str:
        if indx < len(self) and indx >= 0:
            counter = 0
            pointer = self.head
            while counter < indx and pointer.next is not None:
                counter += 1
                pointer = pointer.next
            return pointer.data

    def __len__(self) -> int:
        counter = 0
        pointer = self.head
        while pointer is not None:
            counter += 1
            pointer = pointer.next
        return counter

    def __str__(self) -> str:
        res_head = ''
        res_tail = ''
        pointer = self.head
        while pointer is not None:
            res_head += pointer.data + ' '
            pointer = pointer.next

        pointer = self.tail
        while pointer is not None:
            res_tail += pointer.data + ' '
            pointer = pointer.prev

        return f'head: {res_head}\ntail:{res_tail}'


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert (
    len(ln) == 2
), "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert (
    ln(2) == "Python"
), "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert (
    ln(1) == "Балакирев"
), "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert (
    n == 3
), "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert (
    n == 3
), "при перемещении по списку через __prev не все объекты перебрались"
ln.remove_obj(0)
ln.remove_obj(0)
print(ln)
ln.remove_obj(0)
print(ln)
