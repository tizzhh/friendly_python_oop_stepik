class Model:
    data = None

    def query(self, **kwargs):
        self.data = kwargs

    def __str__(self) -> str:
        if self.data is None:
            return 'Model'
        else:
            return 'Model: ' + ', '.join(
                (str(key) + ' = ' + str(val) for key, val in self.data.items())
            )


model = Model()
model.query(id=1, fio='Sergey', old=33)
print(model)
