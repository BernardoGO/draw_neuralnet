
import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import core.layer

def generate():
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
                  position = model.layers[ind].position
                  )
        core.layer.label(ind, text_list[ind]+ '\n{}@{}x{}'.format(
            model.layers[ind].getFilters(),  model.layers[ind].input_shape[0], model.layers[ind].input_shape[1]), plt, top=True)


    ##Links between layers
    for ind in range(len(core.layer.layers)-1):
        #print([len(core.layer.positions), ind])
        core.layer.add_mapping(patches, colors, start_ratio_list[ind],
                    patch_size_list[ind], ind, ax
                    )
        core.layer.label(ind, text_list[ind]+ '\n{}x{} kernel'.format(
            model.layers[ind].getSize(), model.layers[ind].getSize()), plt, top=False                    
    #-------------------------------------------------------------------------------
    colors += [0, 1]
    print(["P", len(patches), len(colors)])
    #print(patches)
    collection = PatchCollection(patches, cmap=plt.cm.gray)
    collection.set_array(np.array(colors))
    ax.add_collection(collection)
    #ax.add_line(Line2D([0, 50],
    #                      [0, -16]))
    plt.tight_layout()
    #plt.ylim([0,80])
    plt.xlim([0,model.getCount() * core.layer.get_effective_area()])
    plt.axis('off')
    plt.show()

    fig_dir = './'
    fig_ext = '.png'
    fig.savefig(os.path.join(fig_dir, 'figure' + fig_ext),
                bbox_inches='tight', pad_inches=0)

generate()
