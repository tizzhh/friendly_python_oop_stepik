class PhoneNumber:
    def __init__(self, number: int, fio: str) -> None:
        self.number = number
        self.fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if len(str(number)) == 11:
            self.__number = number
        else:
            raise ValueError('Wrong number format')

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        if isinstance(fio, str):
            self.__fio = fio
        else:
            raise ValueError('Fio should be a string')


class PhoneBook:
    numbers = []

    def add_phone(self, phone: PhoneNumber):
        self.numbers.append(phone)

    def remove_phone(self, indx):
        self.numbers.pop(indx)

    def get_phone_list(self):
        return self.numbers


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
