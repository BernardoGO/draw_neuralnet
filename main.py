
import os
import numpy as np
import core.layer
import core.plot
from frameworks.keras.layers import Conv2D, MaxPooling2D, Dense
from frameworks.keras.model import Sequencial

def new():


    core.plot.initPlot()

    model = Sequencial()
    model.add(Conv2D(32, (1, 1), input_shape=(500,500,3), trainable=False))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(2, (3, 3), trainable=False))
    model.add(Conv2D(4, (3, 3), trainable=False))
    model.add(Dense(512, activation='relu'))

    core.plot.gen(model)

    ################
    core.plot.show(model)





new()
