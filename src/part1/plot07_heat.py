import matplotlib.pyplot as plt
import numpy as np

def heat_plot(data=None, cmap="terrain", ax=None, colorbar=True, **imshow_):
    if data is None:
        data = np.random.rand(5, 5)
    data = np.asarray(data)
    if data.ndim !=2:
        raise ValueError('data must be a 2D array')

    if ax is None:
        fig, ax = plt.subplots()

    im = ax.imshow(data, cmap=cmap, **imshow_)

    ax.set_xlabel('column')
    ax.set_ylabel('row')

    if colorbar:
        plt.colorbar(im, ax=ax)

    return im