from typing import Any


class Note:
    ALLOWED_NAMES = (
        'до',
        'ре',
        'ми',
        'фа',
        'соль',
        'ля',
        'си',
    )
    ALLOWED_TONES = (-1, 0, 1)

    def __init__(self, name, ton=0) -> None:
        self._name = name
        self._ton = ton

    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == '_name':
            if __value not in self.ALLOWED_NAMES:
                raise ValueError('недопустимое значение аргумента')
        elif __name == '_ton':
            if __value not in self.ALLOWED_TONES:
                raise ValueError('недопустимое значение аргумента')
        super().__setattr__(__name, __value)


class Notes:
    MIN_INDX = 0
    MAX_INDX = 6

    __slots__ = (
        '_do',
        '_re',
        '_mi',
        '_fa',
        '_solt',
        '_la',
        '_si',
    )

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            for name, val in zip(cls.__slots__, Note.ALLOWED_NAMES):
                setattr(cls.__instance, name, Note(val))
        return cls.__instance

    def _check_indx(func):
        def wrapper(self, *args, **kwargs):
            indx = args[0]
            if (
                not isinstance(indx, int)
                or not self.MIN_INDX <= indx <= self.MAX_INDX
            ):
                raise IndexError('недопустимый индекс')
            return func(self, *args, **kwargs)

        return wrapper

    @_check_indx
    def __getitem__(self, indx):
        return getattr(self, self.__slots__[indx])


notes = Notes()
notes[3]._ton = -1  # изменение тональности ноты фа
