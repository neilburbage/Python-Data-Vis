import matplotlib.pyplot as plt
import numpy as np

def line_plot(x=None, y=None, ax=None):

    if x is None or y is None:
        x = np.arange(1,6)
        y = np.array([10, 12, 5, 8, 7])

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.plot(x, y, marker="o")
    ax.set(
        xlabel="X-axis",
        ylabel="Y-axis",
        title="Line Plot Example",
    )
    return fig