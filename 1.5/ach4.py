from random import randint

class Line:
    def __init__(self, a=0, b=0, c=0, d=0) -> None:
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a=0, b=0, c=0, d=0) -> None:
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a=0, b=0, c=0, d=0) -> None:
        self.sp = (a, b)
        self.ep = (c, d)

classes = {
    0: Line,
    1: Rect,
    2: Ellipse,
}

elements = []
for _ in range(217):
    class_name = classes[randint(0, 2)]
    if class_name is Line:
        elements.append(class_name())
    else:
        elements.append(class_name(1, 2, 3, 4))
