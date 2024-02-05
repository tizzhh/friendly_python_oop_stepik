class ListInteger(list):
    def __init__(self, *args):
        if any(not isinstance(x, int) for x in args[0]):
            raise TypeError('можно передавать только целочисленные значения')
        super().__init__(*args)

    def __setitem__(self, indx, val):
        if not isinstance(val, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(indx, val)

    def append(self, obj):
        if not isinstance(obj, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().append(obj)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(11)
print(s)
