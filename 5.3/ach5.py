from typing import Union


class Test:
    MIN_LENGTH = 10
    MAX_LENGTH = 10_000

    def __init__(self, descr: str) -> None:
        if not self.MIN_LENGTH <= len(descr) <= self.MAX_LENGTH:
            raise ValueError(
                'формулировка теста должна быть от 10 до 10 000 символов'
            )
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(
        self,
        descr: str,
        ans_digit: Union[int, float],
        max_error_digit: float = 0.01,
    ) -> None:
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit
        self.__check_args()

    def __check_args(self):
        if (
            type(self.ans_digit) not in (int, float)
            or type(self.max_error_digit) not in (int, float)
            or not self.max_error_digit >= 0
        ):
            raise ValueError('недопустимые значения аргументов теста')

    def run(self) -> bool:
        ans = float(input())
        return (
            self.ans_digit - self.max_error_digit
            <= ans
            <= self.ans_digit + self.max_error_digit
        )


descr, ans = map(
    str.strip, input().split('|')
)  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(
    ans
)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

try:
    test = TestAnsDigit(descr, ans)
    print(test.run())
except Exception as e:
    print(e)
