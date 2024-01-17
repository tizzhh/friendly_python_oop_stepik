class SingletonFive:
    count = 0
    last_obj = None

    def __new__(cls, *args, **kwargs):
        if cls.count < 5:
            cls.last_obj = super().__new__(cls)
        cls.count += 1
        return cls.last_obj

    def __init__(self, name) -> None:
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
