from typing import Union


class DigitRetrieve:
    def __call__(self, value: str) -> Union[None, int]:
        try:
            return int(value)
        except ValueError:
            return None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "--5"]
digits = list(map(dg, st))
print(digits)
