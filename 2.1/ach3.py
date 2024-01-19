class Clock:
    def __init__(self, time=0) -> None:
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def __check_time(cls, tm):
        return isinstance(tm, int) and 0 <= tm <= 100000


clock = Clock(4530)
