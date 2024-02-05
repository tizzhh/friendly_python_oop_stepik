class IteratorAttrs:
    def __iter__(self):
        for key, val in self.__dict__.items():
            yield (key, val)


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory) -> None:
        self.model = model
        self.size = size
        self.memory = memory


phone = SmartPhone('aboba', 1, 2)
for attr, value in phone:
    print(attr, value)
