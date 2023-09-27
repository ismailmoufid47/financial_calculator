import matplotlib.pyplot as plt


def plot_values_over_time(tuple):
    times, values, label, xlabel, ylabel, title, text_x, text_y, text_label = tuple
    plt.plot(times, values, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.text(text_x, text_y, text_label, fontsize=12, ha="right")
    plt.legend()
    plt.show()
