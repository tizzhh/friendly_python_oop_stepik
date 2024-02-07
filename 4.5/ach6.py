from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        ...

    def get_info(self):
        return 'Базовый класс Model'


class ModelForm(Model):
    _id = 0

    def __init__(self, login, password) -> None:
        self._login = login
        self._password = password
        self._id = type(self)._id
        type(self)._id += 1

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())
