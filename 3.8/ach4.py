from typing import Callable, List, Union


def check_indx(func: Callable):
    def wrapper(self, *args, **kwargs):
        indx = args[0]
        if not isinstance(indx, int) or not 0 <= indx < self.max_length:
            raise IndexError('неверный индекс для доступа к элементам массива')
        return func(self, *args, **kwargs)

    return wrapper


class BaseCell:
    data_type = None
    default_val = None
    err_msg = ''

    def __init__(self, start_value: Union[int, float] = None) -> None:
        self.__start_value = start_value or self.default_val

    @property
    def value(self) -> Union[int, float]:
        return self.__start_value

    @value.setter
    def value(self, val: Union[int, float]) -> None:
        if not isinstance(val, self.data_type):
            raise ValueError(self.err_msg)
        self.__start_value = val


class Float(BaseCell):
    data_type = float
    default_val = 0.0
    err_msg = 'должно быть целое или рациональное число'


class Integer(BaseCell):
    data_type = int
    default_val = 0
    err_msg = 'должно быть целое число'


class Array:
    def __init__(self, max_length: int, cell: Integer) -> None:
        self.max_length = max_length
        self.array: List[Integer] = [cell() for _ in range(max_length)]

    @check_indx
    def __getitem__(self, indx: int) -> int:
        return self.array[indx].value

    @check_indx
    def __setitem__(self, indx: int, val: int) -> None:
        self.array[indx].value = val

    def __str__(self) -> str:
        return ' '.join([str(val.value) for val in self.array])


ar_int = Array(10, cell=Integer)
print(ar_int[3])
print(ar_int)
ar_int[1] = 10
print(ar_int)


ar_float = Array(5, cell=Float)
print(ar_float[3])
print(ar_float)
ar_float[1] = 115.123
print(ar_float)
