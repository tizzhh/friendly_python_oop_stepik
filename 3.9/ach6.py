def sum_kinda(val):
    if val == 1:
        return 1
    return val + sum_kinda(val - 1)


class TriangleListIterator:
    def __init__(self, lst) -> None:
        self.lst = lst
        self.rows = len(lst)

    def __iter__(self):
        self.elems = 0
        self._i = 0
        self._j = 0
        return self

    def __next__(self):
        if self.elems < sum_kinda(self.rows):
            val = self.lst[self._i][self._j]
            if self._j <= self._i:
                self._j += 1
            if self._j > self._i:
                self._i += 1
                self._j = 0
            self.elems += 1
            return val
        else:
            raise StopIteration


lst = [
    [0],
    [1, 2],
    [3, 4, 5],
]
it = TriangleListIterator(lst)
for x in it:
    print(x)
