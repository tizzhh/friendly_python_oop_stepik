from typing import Union


class TeleDescriptor:
    def __set_name__(self, owner, name) -> None:
        self.name = '__' + name

    def __get__(self, instance, owner) -> Union[int, str]:
        return (
            getattr(instance, self.name)
            if instance is not None
            else property()
        )

    def __set__(self, instance, name) -> None:
        setattr(instance, self.name, name)


class Telecast:
    uid = TeleDescriptor()
    name = TeleDescriptor()
    duration = TeleDescriptor()

    def __init__(self, id: int, name: str, duration: int) -> None:
        self.uid = id
        self.name = name
        self.duration = duration


class TVProgram:
    def __init__(self, name: str) -> None:
        self.name = name
        self.items: list[Telecast] = []

    def add_telecast(self, tl: Telecast) -> None:
        self.items.append(tl)

    def remove_telecast(self, indx) -> None:
        indxes = [telecast for telecast in self.items if telecast.uid == indx]
        if indxes:
            self.items.remove(indxes[0])


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.remove_telecast(1)
for t in pr.items:
    print(f"{t.name}: {t.duration}")
