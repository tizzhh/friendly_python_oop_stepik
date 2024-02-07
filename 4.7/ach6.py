class Star:
    __slots__ = ('_name', '_massa', '_temp')

    def __init__(self, name, massa, temp) -> None:
        self._name = name
        self._massa = massa
        self._temp = temp


class StarMixin(Star):
    __slots__ = (
        '_type_star',
        '_radius',
    )

    def __init__(self, name, massa, temp, type_star, radius) -> None:
        super().__init__(name, massa, temp)
        self._type_star = type_star
        self._radius = radius


class WhiteDwarf(StarMixin):
    __slots__ = ()


class YellowDwarf(StarMixin):
    __slots__ = ()


class RedGiant(StarMixin):
    __slots__ = ()


class Pulsar(StarMixin):
    __slots__ = ()


stars = [
    RedGiant('Альдебаран', 5, 3600, 'красный гигант', 45),
    WhiteDwarf('Сириус А', 2.1, 9250, 'белый карлик', 2),
    WhiteDwarf('Сириус B', 1, 8200, 'белый карлик', 0.01),
    YellowDwarf('Солнце', 1, 6000, 'желтый карлик', 1),
]
white_dwarfs = list(filter(lambda x: isinstance(x, WhiteDwarf), stars))
