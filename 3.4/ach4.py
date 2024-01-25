from typing import Union

from typing_extensions import Self


class NewList:
    def __init__(self, lst: list = []) -> None:
        self.lst = lst

    def __sub__(self, other: Union[Self, list]) -> Self:
        if not isinstance(other, (list, self.__class__)):
            raise TypeError(
                f'Other should be a list or {self.__class__.__name__} type'
            )
        oth_lst = other
        if isinstance(other, self.__class__):
            oth_lst = other.get_list()

        return self.__class__(self.list_sub(self.lst, oth_lst))

    def __rsub__(self, other: Union[Self, list]) -> Self:
        if not isinstance(other, (list, self.__class__)):
            raise TypeError(
                f'Other should be a list or {self.__class__.__name__} type'
            )
        oth_lst = other
        if isinstance(other, self.__class__):
            oth_lst = other.get_list()

        return self.__class__(self.list_sub(oth_lst, self.lst))

    @staticmethod
    def list_sub(lst: list, oth_lst: list) -> list:
        oth_lst = [(elem, type(elem)) for elem in oth_lst]
        return [
            elem
            for elem in lst
            if not (elem, type(elem)) in oth_lst
            or oth_lst.remove((elem, type(elem)))
        ]

    def get_list(self) -> list:
        return self.lst


lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
lst2 = NewList([0, 1, 2, 3, True])
res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(res_1.get_list())
lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
print(lst1.get_list())
res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
print(res_2.get_list())
res_3 = [1, 2, 3, 4.5] - res_2  # NewList: [4.5]
print(res_3.get_list())
a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
print(res_4.get_list())
