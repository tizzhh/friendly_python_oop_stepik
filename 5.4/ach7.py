from typing import Self


class CellException(Exception):
    ...


class CellIntegerException(CellException):
    ...


class CellFloatException(CellException):
    ...


class CellStringException(CellException):
    ...


class BaseCellNum:
    def __init__(self, *args) -> None:
        for key, val in zip(self.atrs, args):
            setattr(self, key, val)
        self._value = None

    @property
    def value(self) -> int | float | str:
        return self._value

    @value.setter
    def value(self, val: int | float | str) -> None:
        if hasattr(self, '_min_value'):
            if not self._min_value <= val <= self._max_value:
                raise self.exc_type('значение выходит за доступный диапазон')
        elif hasattr(self, '_min_length'):
            if not self._min_length <= len(val) <= self._max_length:
                raise self.exc_type('значение выходит за доступный диапазон')
        self._value = val


class CellInteger(BaseCellNum):
    atrs = ('_min_value', '_max_value')
    exc_type = CellIntegerException


class CellFloat(BaseCellNum):
    atrs = ('_min_value', '_max_value')
    exc_type = CellFloatException


class CellString(BaseCellNum):
    atrs = ('_min_length', '_max_length')
    exc_type = CellStringException


class TupleData:
    def __init__(self, *args) -> None:
        self.data = list(args)

    def __getitem__(self, indx: int) -> int | float | str:
        self._check_indx(indx)
        return self.data[indx]

    def __setitem__(self, indx: int, val: int | float | str) -> None:
        self._check_indx(indx)
        self.data[indx] = val

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Self:
        self.__counter = 0
        return self

    def __next__(self) -> int | float | str:
        if self.__counter < len(self):
            val = self.data[self.__counter]
            self.__counter += 1
            return val
        else:
            raise StopIteration

    def _check_indx(self, indx: int) -> None:
        if not 0 <= abs(indx) < len(self):
            raise IndexError


ld = TupleData(
    CellInteger(0, 10),
    CellInteger(11, 20),
    CellFloat(-10, 10),
    CellString(1, 100),
)

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException:
    print("Ошибка при обращении к ячейке")
except Exception:
    print("Общая ошибка при работе с объектом TupleData")
