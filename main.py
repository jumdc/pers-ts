from src.filtration import Filtration

from matplotlib import pyplot as plt

if __name__ == '__main__':
    filtration = Filtration([-10, 0, 5, 0, 0, 19, 0, 0])
    plt.plot(filtration.data)
    filtration.compute_persistence()

    print(filtration.persistence)

    # ax = filtration._plot_persistence_diagram()
    # plt.savefig("test.png")