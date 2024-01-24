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
        if indx >= len(self) or indx < 0:
            raise IndexError('Out of range')

        if self.head is None or self.tail is None:
            return

        pointer = self.head
        for _ in range(indx):
            if pointer.next is None:
                break
            pointer = pointer.next

        if pointer.prev is not None:
            pointer.prev.next = pointer.next
        else:
            self.head = pointer.next

        if pointer.next is not None:
            pointer.next.prev = pointer.prev
        else:
            self.tail = pointer.prev
            self.tail.next = None

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
