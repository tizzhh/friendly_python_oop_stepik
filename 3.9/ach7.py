class IterColumn:
    def __init__(self, lst, column) -> None:
        self.lst = lst
        self.column = column

    def __iter__(self):
        self.__row = 0
        return self

    def __next__(self):
        if self.__row < len(self.lst):
            val = self.lst[self.__row][self.column]
            self.__row += 1
            return val
        else:
            raise StopIteration
