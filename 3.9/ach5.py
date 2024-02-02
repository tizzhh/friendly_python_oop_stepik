class Person:
    def check_indx(func):
        def wrapper(self, *args, **kwargs):
            indx = args[0]
            if not 0 <= indx <= 4:
                raise IndexError('неверный индекс')
            return func(self, *args, **kwargs)

        return wrapper

    def __init__(self, fio, job, old, salary, year_job) -> None:
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__indx = 0

    @check_indx
    def __getitem__(self, indx: int):
        return self.__dict__[tuple(self.__dict__)[indx]]

    @check_indx
    def __setitem__(self, indx: int, val):
        self.__dict__[tuple(self.__dict__)[indx]] = val

    def __iter__(self):
        self.__indx = 0
        return self

    def __next__(self):
        if self.__indx < len(self.__dict__) - 1:
            val = self[self.__indx]
            self.__indx += 1
            return val
        else:
            raise StopIteration


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
print(pers[0])
for v in pers:
    print(v)
for v in pers:
    print(v)
