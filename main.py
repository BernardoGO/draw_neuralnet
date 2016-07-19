
import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import core.layer

def new():
    patches = []
    colors = []
    plt.tight_layout()
    plt.axis('equal')
    #plt.ylim([0,80])

    plt.axis('off')
    plt.show()
