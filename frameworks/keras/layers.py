max_kernel_size_x = 0
max_kernel_size_y = 0
max_filters = 0

import frameworks.keras.layers

class Conv2D():
    def __init__(self, filters,
                kernel_size,
                strides=(1, 1),
                padding='valid',
                data_format=None,
                dilation_rate=(1, 1),
                activation=None,
                use_bias=True,
                input_shape = (None, None, None),
                trainable = True,
                kernel_initializer='glorot_uniform',
                bias_initializer='zeros',
                kernel_regularizer=None,
                bias_regularizer=None,
                activity_regularizer=None,
                kernel_constraint=None,
                bias_constraint=None):
        self.filters = filters
        if filters > frameworks.keras.layers.max_filters:
            frameworks.keras.layers.max_filters = filters

        self.kernel_size = kernel_size
        if kernel_size[0] > frameworks.keras.layers.max_kernel_size_x:
            frameworks.keras.layers.max_kernel_size_x = kernel_size[0]
        if kernel_size[1] > frameworks.keras.layers.max_kernel_size_y:
            frameworks.keras.layers.max_kernel_size_y = kernel_size[1]

        self.input_shape = input_shape

        self.strides = strides
        self.padding = padding
        self.data_format = data_format
        self.dilation_rate = dilation_rate
        self.activation = activation
        self.use_bias = use_bias
        self.kernel_initializer = kernel_initializer
        self.bias_initializer = bias_initializer
        self.kernel_regularizer = kernel_regularizer
        self.bias_regularizer = bias_regularizer
        self.activity_regularizer = activity_regularizer
        self.kernel_constraint = kernel_constraint
        self.bias_constraint = bias_constraint
        self.titleText = "Feature\nmaps"
        self.mappingText = "2D Convolution"

    def setInput_shape(self, input_shape):
        self.input_shape = input_shape

    def getOutputShape(self):
        return (self.input_shape[0]-2,self.input_shape[1]-2,self.filters)

    def getSize(self):
        return self.kernel_size[0]
    def getFilters(self):
        return self.filters

class MaxPooling2D():
    def __init__(self,
                pool_size=(2, 2),
                strides=None,
                padding='valid',
                input_shape = (None, None, None),
                data_format=None):
        self.input_shape = input_shape
        self.pool_size = pool_size
        self.strides = strides
        self.padding = padding
        self.data_format = data_format
        self.titleText = "Feature\nmaps"
        self.mappingText = "2D Max-Pooling"
        self.filters = input_shape[2]

    def setInput_shape(self, input_shape):
        self.input_shape = input_shape
        self.filters = input_shape[2]

    def getOutputShape(self):
        return (self.input_shape[0]/2,self.input_shape[1]/2,self.filters)

    def getSize(self):
        return self.pool_size[0]
    def getFilters(self):
        return self.filters
