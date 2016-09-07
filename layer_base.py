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
