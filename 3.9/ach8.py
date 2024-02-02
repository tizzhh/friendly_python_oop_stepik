class StackObj:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def check_indx(func):
        def wrapper(self, *args, **kwargs):
            indx = args[0]
            if not 0 <= indx < self._size:
                raise IndexError('неверный индекс')
            return func(self, *args, **kwargs)

        return wrapper

    def __init__(self) -> None:
        self.top = None
        self._size = 0

    def __iter__(self):
        self._elems_passed = 0
        self._ptr = self.top
        return self

    def __next__(self):
        if self._elems_passed < self._size:
            obj = self._ptr
            self._elems_passed += 1
            self._ptr = self._ptr.next
            return obj
        else:
            raise StopIteration

    @check_indx
    def __getitem__(self, indx: 0):
        return self.__get_obj(indx).data

    @check_indx
    def __setitem__(self, indx: 0, value):
        self.__get_obj(indx).data = value

    def __get_obj(self, indx):
        ptr = self.top
        for i in range(self._size):
            if i == indx:
                return ptr
            ptr = ptr.next

    def push_back(self, obj: StackObj):
        if self.top is None:
            self.top = obj
        else:
            ptr = self.top
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = obj
        self._size += 1

    def push_front(self, obj: StackObj):
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj
        self._size += 1
