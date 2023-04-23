from src.filtration import Filtration

from matplotlib import pyplot as plt

if __name__ == '__main__':
    filtration = Filtration([-10, 0, 5, 0, 0, 19, 0, 0])
    filtration.compute_persistence()
    ax = filtration._plot_persistence_diagram()
    plt.savefig("test.png")