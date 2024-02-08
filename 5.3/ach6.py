class TupleLimit(tuple):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, lst, max_length) -> None:
        self.lst = lst
        self.max_length = max_length

        if len(lst) > max_length:
            raise ValueError(
                'число элементов коллекции превышает заданный предел'
            )

    def __str__(self) -> str:
        return ' '.join(map(str, self.lst))

    def __repr__(self) -> str:
        return ' '.join(map(str, self.lst))


digits = list(map(float, input().split()))

try:
    tpl = TupleLimit(digits, 5)
except Exception as e:
    print(e)
else:
    print(tpl)
