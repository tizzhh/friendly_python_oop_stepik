class ValidatorString:
    def __init__(self, min_length, max_length, chars) -> None:
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if not self.min_length <= len(string) <= self.max_length or (
            self.chars and not set(self.chars) & set(string)
        ):
            raise ValueError('недопустимая строка')


class LoginForm:
    def __init__(self, login_validator, password_validator) -> None:
        self.login_validator = login_validator
        self.password_validator = password_validator

    def form(self, request):
        if not 'login' in request or not 'password' in request:
            raise TypeError('в запросе отсутствует логин или пароль')
        login, passw = request['login'], request['password']
        self.login_validator.is_valid(login)
        self.password_validator.is_valid(passw)
        self._login = login
        self._password = passw


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
print(login, password)
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
