from random import choice, randint
from typing import Any


class RandomPassword:
    def __init__(
        self, psw_chars: str, min_lenght: int, max_length: int
    ) -> None:
        self.psw_chars = psw_chars
        self.min_length = min_lenght
        self.max_length = max_length

    def __call__(self, *args: Any, **kwds: Any) -> str:
        res = ''
        for _ in range(randint(self.min_length, self.max_length)):
            res += choice(self.psw_chars)
        return res


rnd = RandomPassword('qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*', 5, 20)
lst_pass = [rnd() for _ in range(3)]
print(lst_pass)
