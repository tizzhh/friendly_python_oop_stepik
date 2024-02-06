class AnimalDescr:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Animal:
    name = AnimalDescr()
    kind = AnimalDescr()
    old = AnimalDescr()

    def __init__(self, name, kind, old) -> None:
        self.name = name
        self.kind = kind
        self.old = old


animals = [
    Animal('Васька', 'дворовый кот', 5),
    Animal('Рекс', 'немецкая овчарка', 8),
    Animal('Кеша', 'попугай', 3),
]
