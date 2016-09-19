import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import keras_layers
import sys


layer_width = 40
layer_margin = 10

positions = 0

layers = []

class layer():
    def __init__(self,visible_top, visible_bottom,visible_left,visible_right,size_x,size_y):
        self.visible_top = visible_top
        self.visible_bottom = visible_bottom
        self.visible_left = visible_left
        self.visible_right = visible_right
        self.actual_left = float('inf')
        self.actual_top = float('-inf')
        self.actual_bottom = float('-inf')
        self.size_x = size_x
        self.size_y = size_y

def get_effective_area():
    return layer_width - layer_margin

def add_layer(patches, colors, size=24, num=5,
              position = 0
              ):

    size = (size/keras_layers.max_kernel_size_x)*get_effective_area()
    xue = [size/15,-1*size/15]


    top_left = [position*layer_width, position]

    top_left = np.array(top_left)
    xue = np.array(xue)
    tp = np.array([0, size])
    loc_start = top_left - tp

    post = loc_start + num * xue

    left = post[0]
    bottom = post[1]
    top = bottom+size
    right = left + size
    objlay = layer(top, bottom, left, right,size,size)

    for ind in range(num):
        pos = loc_start + ind * xue
        patches.append(Rectangle(pos, size, size))
        if ind % 2:
            colors.append(Medium)
        else:
            colors.append(Light)
        if pos[0] < objlay.actual_left:
            objlay.actual_left = pos[0]
        if pos[1] > objlay.actual_bottom:
            objlay.actual_bottom = pos[1]
