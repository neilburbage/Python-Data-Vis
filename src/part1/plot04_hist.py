import matplotlib.pyplot as plt
import numpy as np

def hist_plot(data=None, bins='auto', ax=None):
    if data is None:
        data = [2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7]

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.hist(data, bins=bins, alpha=0.7, edgecolor="black")
    ax.set(
        xlabel="Value",
        ylabel="Frequency",
        title="Histogram Plot Example"
    )
    return fig