from typing import Callable, Union


from typing_extensions import Self


def comparing(func: Callable):
    def wrapper(instance: 'Body', other: 'Body'):
        if isinstance(other, (int, float)):
            return func(instance, other)
        elif isinstance(other, Body):
            return func(instance, other.body_mass())
        else:
            raise TypeError('Unsupported Type')

    return wrapper


class Body:
    def __init__(
        self, name: str, ro: Union[int, float], volume: Union[int, float]
    ) -> None:
        self.name = name
        self.ro = ro
        self.volume = volume

    @comparing
    def __lt__(self, other: Union[int, Self]) -> bool:
        return self.body_mass() < other

    @comparing
    def __eq__(self, other: Union[int, Self]) -> bool:
        return self.body_mass() == other

    def body_mass(self) -> float:
        return self.ro * self.volume


body = Body('aboba', 12, 150)
body2 = Body('aboba', 12, 1300)
print(body < body2)
