from random import choice, randint
from string import ascii_letters, digits


class EmailValidator:
    CHARS = ascii_letters + digits + '_' + '.'

    def __new__(cls):
        return None

    @classmethod
    def get_random_email(cls):
        email = ''
        for _ in range(randint(0, 100)):
            email += choice(cls.CHARS)
        return email + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if '@' not in email:
            return False
        try:
            before, after = email.split('@')
        except ValueError:
            return False
        if (
            set(email) <= set(cls.CHARS + '@')
            and len(before) <= 100
            and len(after) <= 50
            and '.' in after
            and cls.__check_dot(email)
        ):
            return True
        return False

    @classmethod
    def __check_dot(cls, email):
        dot_fount = False
        for elem in email:
            if elem == '.' and dot_fount:
                return False
            elif elem != '.':
                dot_fount = False
            elif elem == '.':
                dot_fount = True
        return True

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


print(EmailValidator.is_email_str('abc'))
