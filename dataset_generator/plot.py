import matplotlib.pyplot as plt


def plot_func(t, data):
    plt.style.use('dark_background')
    plt.plot(range(t), data, '-')
    plt.xlabel('t[s]')
    plt.ylabel('P[W]')
    plt.show()

    return None
