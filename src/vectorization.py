import sys

import gudhi.representations
import numpy as np
import pyrootutils

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

from src.persistence import Persistence



def _persistent_image(persitence_values, hyperparams):
    pi_transformer = gudhi.representations.PersistenceImage(
        bandwidth=hyperparams["bandwidth"],
        weight=hyperparams['weight'], # no weight
        resolution=hyperparams["resolution"],
    )
    res = pi_transformer.fit_transform(persitence_values)
    res = res.reshape(
        (res.shape[0], hyperparams["resolution"][0] ,  hyperparams["resolution"][1])
    ) # reshape as a 2D image
    res = np.flip(res, axis=1) # flip the images
    return res

def _betti_curve(persistence_values, hyperparams):
    bc_transformer = gudhi.representations.BettiCurve(
        resolution=hyperparams["resolution"],
        sample_range=hyperparams["sample_range"],
    )
    res = bc_transformer.fit_transform(persistence_values)

    return res