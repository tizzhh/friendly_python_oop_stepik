class VideoItem:
    def __init__(self, title, descr, path) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self) -> None:
        self.rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, val):
        if not isinstance(val, int) or not 0 <= val <= 5:
            raise ValueError('неверное присваиваемое значение')
        self.__rating = val


v = VideoItem(
    'Курс по Python ООП',
    'Подробный курс по Python ООР',
    'D:/videos/python_oop.mp4',
)
print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
descr = v.descr
