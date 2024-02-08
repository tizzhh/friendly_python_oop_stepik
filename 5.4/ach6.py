from datetime import datetime


class DateError(Exception):
    ...


class DateString:
    def __init__(self, date_string) -> None:
        try:
            self.date = datetime.strptime(date_string, '%d.%m.%Y').strftime(
                '%d.%m.%Y'
            )
        except ValueError:
            raise DateError("Неверный формат даты")

    def __str__(self) -> str:
        return self.date


date_string = input()
try:
    date = DateString(date_string)
except DateError as e:
    print(e)
else:
    print(date)
