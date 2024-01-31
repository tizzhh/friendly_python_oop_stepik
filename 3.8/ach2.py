from typing import Any, Callable


def check_index(func: Callable):
    def wrapper(self, *args, **kwargs):
        if not isinstance(args[0], (int, float)) or args[0] >= len(
            self.__dict__
        ):
            raise IndexError('неверный индекс поля')
        return func(self, *args, **kwargs)

    return wrapper


class Record:
    def __init__(self, **kwargs) -> None:
        self.__dict__ = kwargs

    @check_index
    def __getitem__(self, item: int) -> Any:
        for i, v in enumerate(self.__dict__.values()):
            if item == i:
                return v

    @check_index
    def __setitem__(self, key: int, value: Any) -> None:
        for i, k in enumerate(self.__dict__):
            if key == i:
                self.__dict__[k] = value
                return


r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)
r[0] = 2  # доступ к полю pk
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author
print(r[0])  # Супер курс по ООП
# r[3] # генерируется исключение IndexError
