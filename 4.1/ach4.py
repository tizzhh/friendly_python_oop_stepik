class Animal:
    def __init__(self, name, old) -> None:
        self.name = name
        self.old = old

    def get_info(self):
        return f'{self.name}: {self.old}, '


class Cat(Animal):
    def __init__(self, name, old, color, weight) -> None:
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return super().get_info() + f'{self.color}, {self.weight}'


class Dog(Animal):
    def __init__(self, name, old, breed, size) -> None:
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return super().get_info() + f'{self.breed}, {self.size}'
