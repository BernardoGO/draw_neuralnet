import matplotlib.pyplot as plt

from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection


patches = []
colors = []


def initPlot():
    plt.rcdefaults()


    fig, ax = plt.subplots()
    return [fig, ax, patches, colors]
