from string import ascii_lowercase, digits


class LengthValidator:
    def __init__(self, min_length: int, max_length: int) -> None:
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, string: str) -> bool:
        return self.__min_length <= len(string) <= self.__max_length


class CharsValidator:
    def __init__(self, chars: str) -> None:
        self.__chars = chars

    def __call__(self, string: str) -> bool:
        return set(string) <= set(self.__chars)


class LoginForm:
    def __init__(
        self,
        name: str,
        validators: list[LengthValidator, CharsValidator] = None,
    ) -> None:
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request: dict[str, str]) -> None:
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self) -> bool:
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


lg = LoginForm(
    "Вход на сайт",
    validators=[
        LengthValidator(3, 50),
        CharsValidator(ascii_lowercase + digits),
    ],
)
lg.post({"login": "root", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")
