class StringDigit(str):
    def __init__(self, arg) -> None:
        if any(not char.isdigit() for char in arg):
            raise ValueError("в строке должны быть только цифры")
        super().__init__()

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    def __radd__(self, other):
        return self.__class__(other).__add__(self)


sd = StringDigit("123")
print(sd)  # 123
sd = sd + "456"  # StringDigit: 123456
sd = "789" + sd  # StringDigit: 789123456
print(sd)
# sd = sd + "12f"  # ValueError
