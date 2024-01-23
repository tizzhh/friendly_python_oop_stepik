class ValidateString:
    def __init__(self, min_length=0, max_length=0) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return (
            isinstance(string, str)
            and self.min_length <= len(string) <= self.max_length
        )


class StringValue:
    def __init__(self, validator) -> None:
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validator=ValidateString(0, 100))
    password = StringValue(validator=ValidateString(0, 100))
    email = StringValue(validator=ValidateString(0, 100))

    def __init__(self, login, password, email) -> None:
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [field for field in self.__dict__.values()]

    def show(self):
        print(
            f'''<form>
            Логин: {self.login}
            Пароль: {self.password}
            Email: {self.email}
            </form>'''
        )
