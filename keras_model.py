class Sequencial:
    def __init__(self):
        self.layers = []
        self.count = 0

    def add(self, layer):
        layer.position = self.count
        self.layers.append(layer)
        self.count += 1
