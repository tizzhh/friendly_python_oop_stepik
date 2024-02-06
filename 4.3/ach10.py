class ItemAttrs:
    def __getitem__(self, indx):
        if abs(indx) < len(list(self.__dict__)):
            return self.__dict__[list(self.__dict__)[indx]]

    def __setitem__(self, indx, val):
        if abs(indx) < len(list(self.__dict__)):
            self.__dict__[list(self.__dict__)[indx]] = val


class Point(ItemAttrs):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]  # 1
y = pt[1]  # 2.5
pt[0] = 10
print(pt.x, pt.y)
