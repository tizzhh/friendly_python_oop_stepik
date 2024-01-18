from string import ascii_lowercase, digits


class Base:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10) -> None:
        self.check_name(name)
        self.name = name
        self.size = size

    @classmethod
    def check_name(cls, name):
        if not 3 <= len(name) <= 50:
            raise ValueError("некорректное поле name")
        if set(name) > set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")


class TextInput(Base):
    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(Base):
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(
            [
                '<form action="#">',
                self.login.get_html(),
                self.password.get_html(),
                '</form>',
            ]
        )


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

print(html)
