from typing import Any, Callable


def check_indx(func: Callable):
    def wrapper(self, *args, **kwargs):
        indx = args[0]
        if not isinstance(indx, int) or not 0 <= indx < self._size:
            raise IndexError('неверный индекс')
        return func(self, *args, **kwargs)

    return wrapper


class StackObj:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top: StackObj = None
        self._size = 0

    def push(self, obj: StackObj) -> None:
        if self.top is None:
            self.top = obj
        else:
            self[self._size - 1].next = obj
        self._size += 1

    def pop(self) -> StackObj:
        res = self[self._size - 1]
        if self[self._size - 2]:
            self[self._size - 2].next = None
        self._size -= 1
        return res

    @check_indx
    def __getitem__(self, indx: int) -> StackObj:
        ptr = self.top
        for i in range(self._size):
            if indx == i:
                return ptr
            ptr = ptr.next
        return None

    @check_indx
    def __setitem__(self, indx: int, new_obj: StackObj) -> None:
        obj_to_change = self[indx]
        new_obj.next = obj_to_change.next
        if self[indx - 1]:
            self[indx - 1].next = new_obj

    def __str__(self) -> str:
        res = ''
        ptr = self.top
        while ptr != None:
            res += str(ptr.data) + ' '
            ptr = ptr.next
        return res


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
print(st)
st[1] = StackObj("newobj2")
print(st)
print(st[2].data)  # obj3
print(st[1].data)  # new obj2
check = st.pop()
print(st)
print(check.data)
