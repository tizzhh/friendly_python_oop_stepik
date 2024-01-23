class Car:
    def __init__(self) -> None:
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and 2 <= len(model) <= 100:
            self.__model = model
