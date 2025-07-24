import matplotlib.pyplot as plt
import numpy as np

def bar_plot(categories=None, values=None, ax=None):

    if categories is None or values is None:
        categories = ['A', 'B', 'C', 'D']
        values = [25, 30, 15, 20]

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.bar(categories, values, alpha=0.7, width=0.6)
    ax.set(
        xlabel='Categories',
        ylabel='Values',
        title='Bar plot Example',
    )
    return fig