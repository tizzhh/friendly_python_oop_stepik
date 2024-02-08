class Validator:
    def __init__(self, min_value, max_value) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, val):
        if (
            type(val) is not self.type_val
            or not self.min_value <= val <= self.max_value
        ):
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    type_val = float


class IntegerValidator(Validator):
    type_val = int


def is_valid(lst, validators):
    res = []
    for val in lst:
        for validator in validators:
            try:
                validator(val)
                res.append(val)
            except:
                continue
    return res


fv = FloatValidator(0, 10.5)
iv = IntegerValidator(-10, 20)
lst_out = is_valid([1, 4.5, 10, 0.5, True], validators=[fv, iv])
print(lst_out)
