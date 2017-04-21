import matplotlib.pyplot as plt

from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import core.plot
import numpy as np

patches = []
colors = []


def initPlot():
    core.plot.plt.rcdefaults()


    core.plot.fig, core.plot.ax = core.plot.plt.subplots()

def show(model):
    core.plot.colors += [0, 1]
    print(["P", len(patches), len(colors)])
    #print(patches)
    collection = PatchCollection(patches, cmap=core.plot.plt.cm.gray)
    collection.set_array(np.array(colors))
    core.plot.ax.add_collection(collection)
    #ax.add_line(Line2D([0, 50],
    #                      [0, -16]))
    core.plot.plt.tight_layout()
    core.plot.plt.axis('equal')
    #plt.ylim([0,80])
    core.plot.plt.xlim([0,model.getCount() * core.layer.get_effective_area()])
    core.plot.plt.axis('off')
    core.plot.plt.show()
