from string import ascii_uppercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_uppercase + digits + ' '

    @classmethod
    def check_name(cls, name: str):
        return (
            set(name) <= set(cls.CHARS_FOR_NAME) and len(name.split(' ')) == 2
        )

    @staticmethod
    def check_card_number(number: str):
        return (
            set(number) <= (set(digits) | set('-'))
            and (all(len(elem) == 4 for elem in number.split('-')))
            and len(number.split('-')) == 4
        )


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
