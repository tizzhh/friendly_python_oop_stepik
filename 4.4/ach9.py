vector_log = []


def class_log(vector_log):
    def logger(func):
        def wrapper(self, *args, **kwargs):
            vector_log.append(func.__name__)
            return func(self, *args, **kwargs)

        return wrapper

    def decorated_cls(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, logger(v))
        return cls

    return decorated_cls


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
# print(v[1])
print(vector_log)
