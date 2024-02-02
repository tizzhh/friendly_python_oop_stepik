import operator as op
from typing import Callable, List, Tuple, Union


class Matrix:
    def check_indx(func: Callable) -> Callable:
        def wrapper(self, *args, **kwargs) -> Union[None, int, float]:
            indx = args[0]
            x, y = indx[0], indx[1]
            if (
                not isinstance(x, int)
                or not isinstance(y, int)
                or not 0 <= x < self.rows
                or not 0 <= y < self.cols
            ):
                raise IndexError('недопустимые значения индексов')
            return func(self, *args, **kwargs)

        return wrapper

    def __init__(self, *args) -> None:
        if len(args) == 3:
            rows, cols, fill_value = args[0], args[1], args[2]
            self.rows: int = rows
            self.cols: int = cols
            self.fill_value: Union[int, float] = fill_value
            self.__check_args()
            self.list2D = [
                [fill_value for _ in range(self.cols)]
                for _ in range(self.rows)
            ]
        elif len(args) == 1:
            self.list2D: List[List[Union[int, float]]] = args[0]
            self.__check_list()
            self.rows = len(self.list2D)
            self.cols = len(self.list2D[0])
        else:
            raise ValueError('unsupported argument')

    @check_indx
    def __getitem__(self, coords: Tuple[int]) -> Union[int, float]:
        x, y = coords[0], coords[1]
        return self.list2D[x][y]

    @check_indx
    def __setitem__(self, coords: Tuple[int], val: Union[int, float]) -> None:
        if not isinstance(val, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        x, y = coords[0], coords[1]
        self.list2D[x][y] = val

    def __add__(self, other: Union['Matrix', int]) -> 'Matrix':
        return self.__do_oper(op.add, other)

    def __sub__(self, other: Union['Matrix', int]) -> 'Matrix':
        return self.__do_oper(op.sub, other)

    def __do_oper(
        self, func: Callable, other: Union[int, 'Matrix'], new_obj: bool = True
    ):
        res_lst = []
        if isinstance(other, Matrix):
            self.__check_dimenstions(other)
            for i in range(len(self.list2D)):
                res_lst += [
                    [
                        func(x, y)
                        for x, y in zip(self.list2D[i], other.list2D[i])
                    ]
                ]
        elif isinstance(other, int):
            for row in self.list2D:
                res_lst += [[func(x, other) for x in row]]
        if new_obj:
            return self.__class__(res_lst)
        else:
            self.list2D = res_lst
            return self

    def __str__(self) -> str:
        res = ''
        for row in self.list2D:
            res += ' '.join(map(str, row)) + '\n'
        return res

    def __check_dimenstions(self, other: 'Matrix') -> None:
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                'операции возможны только с матрицами равных размеров'
            )

    def __check_list(self) -> None:
        cols_one = len(self.list2D[0])
        if not all([len(x) == cols_one for x in self.list2D]):
            raise TypeError(
                'список должен быть прямоугольным, состоящим из чисел'
            )
        for row in self.list2D:
            for val in row:
                if not isinstance(val, (int, float)) or isinstance(val, bool):
                    raise TypeError(
                        'список должен быть прямоугольным, состоящим из чисел'
                    )

    def __check_args(self) -> None:
        if (
            not isinstance(self.rows, int)
            or not isinstance(self.cols, int)
            or not isinstance(self.fill_value, (int, float))
        ):
            raise TypeError(
                'аргументы rows, cols - целые числа; fill_value - произвольное число'
            )


mt = Matrix([[1, 2], [3, 4], [3, 4, 5]])
# mt2 = Matrix([[4, 5], [6, 7]])
# matrix = mt + mt2
# print(matrix)
