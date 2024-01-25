from typing import List, Union


class Thing:
    def __init__(self, name: str, mass: Union[int, float]) -> None:
        self.name = name
        self.mass = mass

    def __eq__(self, other: 'Thing') -> bool:
        return (
            self.name.lower() == other.name.lower() and self.mass == other.mass
        )


class Box:
    def __init__(self) -> None:
        self.__things: List[Thing] = []

    def __eq__(self, other: 'Box') -> bool:
        return sorted(self.things, key=lambda x: (x.mass, x.name)) == sorted(
            other.things, key=lambda x: (x.mass, x.name)
        )

    def add_thing(self, obj: Thing) -> None:
        self.things.append(obj)

    def get_things(self) -> List[Thing]:
        return self.things

    @property
    def things(self) -> List[Thing]:
        return self.__things


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2
print(res)
