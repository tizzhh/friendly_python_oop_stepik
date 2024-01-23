class TriangleChecker:
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        for elem in self.__dict__.values():
            if (
                not isinstance(elem, (int, float))
                or isinstance(elem, bool)
                or elem <= 0
            ):
                return 1
        if (a + b <= c) or (b + c <= a) or (a + c <= b):
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
