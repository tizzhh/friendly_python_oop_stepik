class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self) -> bool:
        x1, y1, x2, y2 = self.x1, self.y1, self.x2, self.y2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 > 1
