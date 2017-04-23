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

def gen(model):
    for ind in range(len(model.layers)):

        core.layer.add_layer(core.plot.patches, core.plot.colors, size=model.layers[ind].getSize(),
                  num=model.layers[ind].getFilters(),
                  position = model.layers[ind].position,
                  titleText = model.layers[ind].titleText+ '\n{}@{}x{}'.format(
                      model.layers[ind].getFilters(),  model.layers[ind].input_shape[0], model.layers[ind].input_shape[1]),
                  mappingText = model.layers[ind].mappingText + '\n{}x{} kernel'.format(
                          model.layers[ind].getSize(), model.layers[ind].getSize())
                  )
        core.layer.label(ind, core.plot.plt, top=True)



    start_ratio_list = [[0.2, 0.1], [0.2, 0.3], [0.4, 0.5], [0.4, 0.8]]
    patch_size_list = [2, 3, 5, 2]
    ind_bgn_list = range(len(patch_size_list))

    for ind in range(len(core.layer.layers)-1):
        #print([len(core.layer.positions), ind])
        core.layer.add_mapping(core.plot.patches, core.plot.colors, start_ratio_list[ind],
                    patch_size_list[ind], ind, core.plot.ax
                    )
        core.layer.label(ind, core.plot.plt, top=False)
