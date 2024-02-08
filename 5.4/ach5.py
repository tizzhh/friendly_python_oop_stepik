class PrimaryKeyError(Exception):
    def __init__(self, *args, **kwargs) -> None:
        id_ = kwargs.get('id', None)
        pk_ = kwargs.get('pk', None)
        self.message = ''
        if id_ is None and pk_ is None:
            self.message = (
                'Первичный ключ должен быть целым неотрицательным числом'
            )
        if id_ is not None:
            self.message = f'Значение первичного ключа id = {id_} недопустимо'
        if pk_ is not None:
            self.message = f'Значение первичного ключа pk = {pk_} недопустимо'

    def __str__(self) -> str:
        return f'{self.message}'


try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as e:
    print(e)
