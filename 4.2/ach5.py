class Protists:
    def __init__(self, name, weight, old) -> None:
        self.name = name
        self.weight = weight
        self.old = old


class Plants(Protists):
    ...


class Mossess(Plants):
    ...


class Flowering(Plants):
    ...


class Animals(Protists):
    ...


class Worms(Animals):
    ...


class Mammals(Animals):
    ...


class Human(Mammals):
    ...


class Monkeys(Mammals):
    ...


class Monkey(Monkeys):
    ...


class Person(Human):
    ...


class Flower(Flowering):
    ...


class Worm(Worms):
    ...


lst_objs = [
    Monkey("мартышка", 30.4, 7),
    Monkey("шимпанзе", 24.6, 8),
    Person("Балакирев", 88, 34),
    Person("Верховный жрец", 67.5, 45),
    Flower("Тюльпан", 0.2, 1),
    Flower("Роза", 0.1, 2),
    Worm("червь", 0.01, 1),
    Worm("червь 2", 0.02, 1),
]

lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]
lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)]
lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]
print(lst_mammals)
