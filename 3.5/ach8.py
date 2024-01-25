from typing import Dict, Union


class CentralBank:
    rates: Dict[str, float] = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls):
        return None

    @classmethod
    def register(cls, money: 'Money'):
        money.cb = cls


class Money:
    MONEY_TYPES = {
        'MoneyR': 'rub',
        'MoneyD': 'dollar',
        'MoneyE': 'euro',
    }

    def __init__(self, money: Union[int, float] = 0) -> None:
        self.volume = money
        self.cb = None

    @property
    def volume(self) -> Union[int, float]:
        return self.__volume

    @volume.setter
    def volume(self, money: Union[int, float]):
        self.__volume = money

    @property
    def cb(self) -> Union[None, CentralBank]:
        return self.__cb

    @cb.setter
    def cb(self, cb: CentralBank) -> None:
        self.__cb = cb

    def __lt__(self, other: 'Money') -> bool:
        if not self.check_registration():
            raise ValueError("Неизвестен курс валют.")
        return self.convert_to_dollar(self.volume) < other.convert_to_dollar(
            other.volume
        )

    def __le__(self, other: 'Money') -> bool:
        if not self.check_registration():
            raise ValueError("Неизвестен курс валют.")
        return self.convert_to_dollar(self.volume) <= other.convert_to_dollar(
            other.volume
        )

    def __eq__(self, other: 'Money') -> bool:
        if not self.check_registration():
            raise ValueError("Неизвестен курс валют.")
        return (
            abs(
                self.convert_to_dollar(self.volume)
                - other.convert_to_dollar(other.volume)
            )
            < 0.1
        )

    def check_registration(self) -> bool:
        return self.cb is not None

    def convert_to_dollar(self, money: float) -> float:
        return money / self.cb.rates[self.MONEY_TYPES[self.__class__.__name__]]


class MoneyR(Money):
    ...


class MoneyD(Money):
    ...


class MoneyE(Money):
    ...


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(700)

CentralBank.register(r)
CentralBank.register(d)
if r > d:
    print("неплохо")
else:
    print("нужно поднажать")

e = MoneyE(300)
CentralBank.register(e)
assert e < d
