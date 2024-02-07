from abc import ABC, abstractmethod, abstractproperty
from typing import Union


class CountryInterface(ABC):
    @abstractproperty
    def name(self):
        ...

    @abstractproperty
    def population(self):
        ...

    @abstractproperty
    def square(self):
        ...

    @abstractmethod
    def get_info(self):
        ...


class Country(CountryInterface):
    def __init__(
        self, name: str, popualtion: int, square: Union[int, float]
    ) -> None:
        self._name = name
        self._population = popualtion
        self._square = square

    @property
    def name(self) -> str:
        return self._name

    @property
    def population(self) -> int:
        return self._population

    @population.setter
    def population(self, val: int) -> None:
        self._population = val

    @property
    def square(self) -> Union[int, float]:
        return self._square

    @square.setter
    def square(self, val: Union[int, float]) -> None:
        self._square = val

    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'


country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info())  # Россия: 354005483.0, 150000000
