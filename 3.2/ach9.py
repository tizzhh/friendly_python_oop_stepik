from typing import Callable


class InputDigits:
    def __init__(self, func: Callable) -> None:
        self.__func = func

    def __call__(self):
        try:
            return [int(num) for num in self.__func().split(' ')]
        except TypeError:
            raise TypeError('В строке присутствуют не только целые числа')


@InputDigits
def input_dg():
    return input()


res = input_dg()
print(res)
