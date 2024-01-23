from typing import Union


class AppVK:
    name = 'ВКонтакте'


class AppYouTube:
    name = 'YouTube'

    def __init__(self, memory_max: int) -> None:
        self.memory_max = memory_max


class AppPhone:
    name = 'Phone'

    def __init__(self, phone_list: dict[str, int]) -> None:
        self.phone_list = phone_list


class SmartPhone:
    def __init__(self, model: str) -> None:
        self.model = model
        self.apps = []

    def add_app(self, app: Union[AppVK, AppYouTube, AppPhone]) -> None:
        if not type(app) in [type(elem) for elem in self.apps]:
            self.apps.append(app)

    def remove_app(self, app: Union[AppVK, AppYouTube, AppPhone]) -> None:
        self.apps.remove(app)


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
