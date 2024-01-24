class PolyLine:
    def __init__(self, *args) -> None:
        self.coords = list(args)

    def add_coord(self, x: int, y: int) -> None:
        self.coords.append((x, y))

    def remove_coord(self, indx: int) -> None:
        self.coords.pop(indx)

    def get_coords(self):
        return self.coords
