import operator as op
from typing import Callable


class Money:
    def __init__(self, val: int | float) -> None:
        self.money = val

    @property
    def money(self) -> int | float:
        return self._money

    @money.setter
    def money(self, val: int | float) -> None:
        if not isinstance(val, (int, float)):
            raise TypeError('сумма должна быть числом')
        self._money = val


class MoneyOperators:
    def __add__(self, other: Money) -> Money:
        return self._do_oper(other, op.add)

    def __sub__(self, other: Money) -> Money:
        return self._do_oper(other, op.sub)

    def _do_oper(self, other: Money, func: Callable) -> Money:
        if isinstance(other, (int, float)):
            return self.__class__(func(self.money, other))

        if type(self) is not type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(func(self.money, other.money))


class MoneyR(Money, MoneyOperators):
    def __str__(self) -> str:
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self) -> str:
        return f"MoneyD: {self.money}"


m1 = MoneyR(1)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
print(m)
