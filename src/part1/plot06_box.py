import matplotlib.pyplot as plt

def box_plot(data=None, labels=None, ax=None, *, vert=True, patch_artist=True):
    if data is None:
        data = [[15, 20, 25, 30, 35, 40, 45, 50]]
    if labels is None:
        labels = ['Age']

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.boxplot(
        data,
        labels=labels,
        vert=vert,
        patch_artist=patch_artist,
        medianprops={'color': 'black'},
    )
    ax.set(
        title='Box plot Example',
        ylabel='Value' if vert else " "
    )
    ax.grid(axis='y', linestyle='--', alpha=0.4
    )
    return fig