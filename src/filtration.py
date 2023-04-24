"""Sub Level set filtration for 1-d Time Series"""


import gudhi
import gudhi.representations
import numpy as np
import matplotlib.pyplot as plt


class Filtration:
    """Class for Sub Level set filtration for 1-d Time Series"""
    def __init__(self, data):
        """
        Initialization

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
        self.data = data
        self.persistence = None

    def compute_persistence(self):
        """
        Computes persistence
        
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
            [
                [ele[1][0], ele[1][1]] 
                if ele[1][1] < np.inf else [ele[1][0], max(self.data)]
                for ele in persistence 
                ]
        )

    def _plot_persistence_diagram(self, save=False, path="figures/pd.png"):
        """
        Plots persistence diagram
        
        Parameters
        ----------
        path : str
            Path to save the plot
        save : bool, optional
            If True, saves the plot, by default False
        """
        gudhi.plot_persistence_diagram(self.persistence)
        if save: 
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

    def persistent_image(self,
                        bandwidth=1,
                        weight=lambda x: 1, # 
                        resolution=[20,20] ):
        """Compute the persistent image."""     

        persistent_im_trf = gudhi.representations.vector_methods.PersistenceImage(
            bandwidth=bandwidth, 
            weight=weight, 
            resolution=resolution
        )
        persistent_image = persistent_im_trf.fit_transform(
            [self.persistence]
        )
        return persistent_image

        
