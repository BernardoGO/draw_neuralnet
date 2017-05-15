import core.layer

class Sequencial:
    def __init__(self):
        self.layers = []
        self.count = 0

    def add(self, layer):
        layer.position = self.count
        if layer.input_shape == (None, None, None):
            layer.setInput_shape(self.layers[layer.position-1].getOutputShape())
        self.layers.append(layer)
        self.count += 1

    def getCount(self):
        return 1+ self.count
