class Triangle:
    def __init__(self, a, b, c) -> None:
        self._a = a
        self._b = b
        self._c = c
        self._check_args(a, b, c)
        self._check_is_triangle(a, b, c)

    @staticmethod
    def _check_args(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or not arg >= 0:
                raise TypeError(
                    'стороны треугольника должны быть положительными числами'
                )

    @staticmethod
    def _check_is_triangle(a, b, c):
        if a < b + c and b < a + c and c < a + b:
            return None
        raise ValueError(
            'из указанных длин сторон нельзя составить треугольник'
        )


input_data = [
    (1.0, 4.54, 3),
    ('abc', 1, 2, 3),
    (-3, 3, 5.2),
    (4.2, 5.7, 8.7),
    (True, 3, 5),
    (7, 4, 6),
]
lst_tr = []
for inp in input_data:
    try:
        lst_tr.append(Triangle(*inp))
    except:
        ...

print(lst_tr)
