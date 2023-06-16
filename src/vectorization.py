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


def _persistent_image(X, hyperparams):
    persistence = Persistence()
    persitence_values = persistence.fit_transform(X)
    pi_transformer = gudhi.representations.PersistenceImage(
        bandwidth=hyperparams["bandwidth"],
        # weight=hyperparams["weight"],
        weight=lambda x : 1, # no weight
        resolution=hyperparams["resolution"],
    )
    res = pi_transformer.fit_transform(persitence_values)
    res = res.reshape(
        (res.shape[0], 1, hyperparams["resolution"][0] ,  hyperparams["resolution"][1])
    ) # reshape as a 2D image

