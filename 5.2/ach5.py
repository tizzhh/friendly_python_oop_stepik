class Point:
    def __init__(self, x=0, y=0) -> None:
        self._x = x
        self._y = y


try:
    a, b = input().split()
    try:
        res = Point(int(a), int(b))
    except:
        res = Point(float(a), float(b))
except:
    res = Point(0, 0)
finally:
    print(f'Point: x = {res._x}, y = {res._y}')
