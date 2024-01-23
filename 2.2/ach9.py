class LineTo:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args) -> None:
        self.path = list(args)

    def get_path(self):
        return self.path

    def get_length(self):
        res = 0
        prev = LineTo(0, 0)
        for elem in self.path:
            res += ((elem.x - prev.x) ** 2 + (elem.y - prev.y) ** 2) ** 0.5
            prev = elem
        return res

    def add_line(self, line):
        self.path.append(line)
