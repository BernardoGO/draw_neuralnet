
import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import core.layer

def generate():
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
