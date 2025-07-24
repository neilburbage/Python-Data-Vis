import matplotlib.pyplot as plt
import numpy as np

def scatter_plot(x=None, y=None, ax=None):
    if x is None or y is None:
        x = [1, 2, 3, 4, 5]
        y = [10, 12, 5, 8, 7]

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.scatter(x,y, alpha=0.7)
    ax.set(title="Scatter Plot Example")
    return fig
