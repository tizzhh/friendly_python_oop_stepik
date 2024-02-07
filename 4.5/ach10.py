from typing import Union


class Food:
    def __init__(
        self, name: str, weight: Union[int, float], calories: int
    ) -> None:
        self._name = name
        self._weight = weight
        self._calories = calories


class BreadFood(Food):
    def __init__(
        self, name: str, weight: Union[int, float], calories: int, white: bool
    ) -> None:
        super().__init__(name, weight, calories)
        self._white = white


class SoupFood(Food):
    def __init__(
        self,
        name: str,
        weight: Union[int, float],
        calories: int,
        dietary: bool,
    ) -> None:
        super().__init__(name, weight, calories)
        self._dietary = dietary


class FishFood(Food):
    def __init__(
        self, name: str, weight: Union[int, float], calories: int, fish: bool
    ) -> None:
        super().__init__(name, weight, calories)
        self._fish = fish
