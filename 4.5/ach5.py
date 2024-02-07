class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val):
        return (
            isinstance(val, (float))
            and self.min_value <= val <= self.max_value
        )


float_validator = FloatValidator(0, 10.5)
res_1 = float_validator(1)  # False (целое число, а не вещественное)
res_2 = float_validator(1.0)  # True
res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
print(res_1, res_2, res_3)
