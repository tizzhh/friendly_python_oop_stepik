from typing import Any, Dict, Union


class Aircraft:
    def __init__(
        self,
        model: str,
        mass: Union[int, float],
        speed: Union[int, float],
        top: Union[int, float],
    ) -> None:
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name in ['_mass', '_speed', '_top']:
            if not isinstance(__value, (int, float)) or not __value > 0:
                raise TypeError('неверный тип аргумента')
        if __name == '_model':
            if not isinstance(__value, str):
                raise TypeError('неверный тип аргумента')
        return super().__setattr__(__name, __value)


class PassengerAircraft(Aircraft):
    def __init__(
        self,
        model: str,
        mass: Union[int, float],
        speed: Union[int, float],
        top: Union[int, float],
        chairs: int,
    ) -> None:
        super().__init__(model, mass, speed, top)
        self._chairs = self.__check_chairs(chairs)

    @staticmethod
    def __check_chairs(chairs) -> int:
        if not isinstance(chairs, int) or not chairs > 0:
            raise TypeError('неверный тип аргумента')
        return chairs


class WarPlane(Aircraft):
    def __init__(
        self,
        model: str,
        mass: Union[int, float],
        speed: Union[int, float],
        top: Union[int, float],
        weapons: Dict[str, int],
    ) -> None:
        super().__init__(model, mass, speed, top)
        self._weapons = self.__check_weapons(weapons)

    @staticmethod
    def __check_weapons(weapons) -> Dict[str, int]:
        if not isinstance(weapons, dict):
            raise TypeError('неверный тип аргумента')
        return weapons


planes = [
    PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
    PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
    WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7}),
]


print(planes)
