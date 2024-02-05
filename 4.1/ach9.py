class Layer:
    def __init__(self, name='Layer') -> None:
        self.next_layer = None
        self.name = name

    def __call__(self, next_layer):
        self.next_layer = next_layer
        return next_layer


class Input(Layer):
    def __init__(self, inputs) -> None:
        super().__init__(name='Input')
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs, outputs, activation) -> None:
        super().__init__(name='Dense')
        self.inputs = input
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, obj) -> None:
        self.obj: Layer = obj

    def __iter__(self):
        self._ptr = self.obj
        return self

    def __next__(self):
        if self._ptr is not None:
            obj = self._ptr
            self._ptr = self._ptr.next_layer
            return obj
        raise StopIteration


network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))
for x in NetworkIterator(network):
    print(x.name)
