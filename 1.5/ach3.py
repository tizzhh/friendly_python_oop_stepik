class Point:
    def __init__(self, x, y, color=None) -> None:
        self.x = x
        self.y = y
        self.color = color

points = []
for i in range(1, 2001, 2):
    points.append(Point(i, i))

points[1].color = 'yellow'