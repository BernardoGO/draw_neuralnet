
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

    fig, ax = plt.subplots()
    from keras_layers import Conv2D
    from keras_model import Sequencial
    import core.layer
    model = Sequencial()
    model.add(Conv2D(32, (1, 1), input_shape=(500,500,3), trainable=False))
    model.add(Conv2D(2, (3, 3), trainable=False))
    model.add(Conv2D(4, (3, 3), trainable=False))

    for ind in range(len(model.layers)):

        core.layer.add_layer(patches, colors, size=model.layers[ind].getSize(),
                  num=model.layers[ind].getFilters(),
                  position = model.layers[ind].position,
                  titleText = model.layers[ind].titleText+ '\n{}@{}x{}'.format(
                      model.layers[ind].getFilters(),  model.layers[ind].input_shape[0], model.layers[ind].input_shape[1]),
                  mappingText = model.layers[ind].mappingText + '\n{}x{} kernel'.format(
                          model.layers[ind].getSize(), model.layers[ind].getSize())
                  )
        core.layer.label(ind, plt, top=True)



    start_ratio_list = [[0.2, 0.1], [0.2, 0.3], [0.4, 0.5], [0.4, 0.8]]
    patch_size_list = [2, 3, 5, 2]
    ind_bgn_list = range(len(patch_size_list))

    for ind in range(len(core.layer.layers)-1):
        #print([len(core.layer.positions), ind])
        core.layer.add_mapping(patches, colors, start_ratio_list[ind],
                    patch_size_list[ind], ind, ax
                    )
        core.layer.label(ind, plt, top=False)

    ################
    colors += [0, 1]
    print(["P", len(patches), len(colors)])
    #print(patches)
    collection = PatchCollection(patches, cmap=plt.cm.gray)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)
    #ax.add_line(Line2D([0, 50],
    #                      [0, -16]))
    plt.tight_layout()
    plt.axis('equal')
    #plt.ylim([0,80])
    plt.xlim([0,model.getCount() * core.layer.get_effective_area()])
    plt.axis('off')
    plt.show()
    #fig.set_size_inches(8, 2.5)



new()
