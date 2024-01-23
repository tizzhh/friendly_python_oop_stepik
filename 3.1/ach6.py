from typing import Union


class Exhibit:
    def __init__(self, name: str, descr: str) -> None:
        self.name = name
        self.descr = descr


class Picture(Exhibit):
    def __init__(self, name: str, author: str, descr: str) -> None:
        super().__init__(name, descr)
        self.author = author


class Mummies(Exhibit):
    def __init__(self, name: str, location: str, descr: str) -> None:
        super().__init__(name, descr)
        self.location = location


class Papyri(Exhibit):
    def __init__(self, name: str, date: str, descr: str) -> None:
        super().__init__(name, descr)
        self.date = date


class Museum:
    def __init__(self, name: str) -> None:
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj: Union[Picture, Mummies, Papyri]) -> None:
        self.exhibits.append(obj)

    def remove_exhibit(self, obj: Union[Picture, Mummies, Papyri]) -> None:
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx: int) -> str:
        obj = self.exhibits[indx]
        return f'Описание экспоната {obj.name} {obj.descr}'


mus = Museum("Эрмитаж")
mus.add_exhibit(
    Picture(
        "Балакирев с подписчиками пишет письмо иноземному султану",
        "Неизвестный автор",
        "Вдохновляющая, устрашающая, волнующая картина",
    )
)
mus.add_exhibit(
    Mummies(
        "Балакирев",
        "Древняя Россия",
        "Просветитель XXI века, удостоенный мумификации",
    )
)
p = Papyri(
    "Ученья для, не злата ради",
    "Древняя Россия",
    "Самое древнее найденное рукописное свидетельство о языках программирования",
)
mus.add_exhibit(p)
for x in mus.exhibits:
    print(x.descr)
print(mus.get_info_exhibit(0))
