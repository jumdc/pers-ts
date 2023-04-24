"""Sub Level set filtration for 1-d Time Series"""


import gudhi
import numpy as np
import gudhi.representations
from sklearn.base import BaseEstimator, TransformerMixin


class Persistence(BaseEstimator, TransformerMixin):
    """Class for Sub Level set filtration for 1-d Time Series"""

    def __init__(self):
        """Initialization"""
        self.simplices = None
        self.is_fitted = False

    def fit(self, X, y=None):
        """
        Simplex tree fit

        Returns
        -------
        simplices : list
            List of simplices (n)
        """

        self.simplices = [self._create_simplex(to_filter) for to_filter in X]
        self.is_fitted = True
        return self

    @staticmethod
    def _create_simplex(data):
        """
        Creates a simplex tree from the 1-d data.

        Parameters
        ----------
        data : list
            1-d data

        Returns
        -------
        simplex : gudhi.SimplexTree
            Simplex tree
        """
        simplex = gudhi.SimplexTree()
        # First we insert the vertices of the time series
        for idx, value in enumerate(data):
            simplex.insert(
                [idx],  # 0-simplex
                filtration=value  # the ordering on our vertices
                # is the values of the time series
            )
        # Second, we insert the edges of the time series
        for idx, value in enumerate(data):
            simplex.insert([idx, idx + 1], filtration=value)  # 1-simplex
        return simplex

    def transform(self, X, y=None):
        """
        Computes the persistence intervals for each filtration

        Returns
        -------
        res : list
            List of persistence intervals for each filtration
        """
        res = [self.compute_persistence(simplex) for simplex in self.simplices]
        return res

    @staticmethod
    def compute_persistence(simplex):
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
        persistence = simplex.persistence()
        maxi = max(
            [filtration_val[1] for filtration_val in simplex.get_filtration()]
        )
        persistence = np.asarray(
            [
                [ele[1][0], ele[1][1]] 
                for ele in persistence
                if ele[1][1] < np.inf # else [ele[1][0], maxi]
            ]
        )
        return persistence
