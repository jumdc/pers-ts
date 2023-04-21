"""Sub Level set filtration for 1-d Time Series"""


import gudhi
import numpy as np
import matplotlib.pyplot as plt


class LevelFiltration:
    """Class for Sub Level set filtration for 1-d Time Series"""
    def __init__(self, data):
        """Initialization

        Parameters
        ----------
        data : list
            Time series data
        """
        self.simplex = gudhi.SimplexTree()
        # First we insert the vertices of the time series
        for idx, value in enumerate(data):
            self.simplex.insert(
                [idx], # 0-simplex
                filtration=value # the ordering on our vertices
                # is the values of the time series
            )
        # Second, we insert the edges of the time series
        for idx, value in enumerate(data):
            self.simplex.insert(
                [idx, idx+1], # 1-simplex
                filtration=value
            )
        self.persistence = None

    def compute_persistence(self):
        """Computes persistence
        
        Parameters
        ----------
        graph : bool, optional
            If True, plots persistence diagram and persistence barcode, by default False

        Returns
        -------
        persistence : list
            List of persistence pairs
        """
        persistence = self.simplex.persistence()
        self.persistence = np.asarray(
            [[ele[1][0], ele[1][1]] for ele in persistence if ele[1][1] < np.inf]
        )

    def _plot_persistence_diagram(self, path="figures/pd.png"):
        """Plots persistence diagram
        
        Parameters
        ----------
        path : str
            Path to save the plot
        """
        gudhi.plot_persistence_diagram(self.persistence)
        plt.savefig(path)

    def _plot_persistence_barcode(self, path="figures/pb.png"):
        """Plots persistence barcode
        
        Parameters
        ----------
        path : str
            Path to save the plot
        """
        gudhi.plot_persistence_barcode(self.persistence)
        plt.savefig(path)

    def vectorize(self):
        """Vectorization of the persistence."""
        pass

if __name__ == "__main__":
    filtration = LevelFiltration([0, 22, 0, 0, 15, 20, 0, 0, 0, 0])
    filtration.compute_persistence()
    filtration._plot_persistence_diagram()
    filtration._plot_persistence_barcode()
