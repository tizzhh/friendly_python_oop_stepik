from math import sqrt


class RadiusVector:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.coords = [0] * args[0]
        else:
            self.coords = list(args)

    def __len__(self) -> int:
        return len(self.coords)

    def __abs__(self) -> float:
        return sqrt(sum(coord * coord for coord in self.coords))

    def set_coords(self, *args) -> None:
        length = (
            len(args) if len(args) < len(self.coords) else len(self.coords)
        )
        for i in range(length):
            self.coords[i] = args[i]

    def get_coords(self) -> tuple[int, float]:
        return tuple(self.coords)
