class CircleDesc:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return property() if instance is None else getattr(instance, self.name)

    def __set__(self, instance, val):
        if not isinstance(val, (int, float)):
            raise TypeError("Неверный тип присваиваемых данных.")
        if self.name == '__radius':
            if val <= 0:
                return
        setattr(instance, self.name, val)


class Circle:
    x = CircleDesc()
    y = CircleDesc()
    radius = CircleDesc()

    def __init__(self, x: int, y: int, radius: int) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def __getattr__(self, __item) -> bool:
        return False


circle = Circle(10.5, 7, 22)
circle.radius = -10
x, y = circle.x, circle.y
res = circle.name
