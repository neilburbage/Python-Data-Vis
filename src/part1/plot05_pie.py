import matplotlib.pyplot as plt

def pie_plot(sizes=None, labels=None, ax=None):
    if sizes is None:
        sizes = [30, 25, 20, 25]
    if labels is None:
        labels = ['A', 'B', 'C', 'D']

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    ax.set(
        title='Pie Chart Example'
    )
    return fig