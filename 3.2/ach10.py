from typing import Callable, Union


class RenderDigit:
    def __call__(self, val: str) -> Union[int, None]:
        try:
            return int(val)
        except ValueError:
            return None


class InputValues:
    def __init__(self, render: Callable):
        self.__render = render

    def __call__(self, func: Callable):
        def wrapper(*args, **kwargs):
            return list(map(self.__render, func().split(' ')))

        return wrapper


@InputValues(RenderDigit())
def input_dg():
    return input()


# render = RenderDigit()
# input_dg = InputValues(render)(input)
res = input_dg()
print(res)
