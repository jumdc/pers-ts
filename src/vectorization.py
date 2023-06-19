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

from filtration import Filtration

sys.path.append("/home/jmordacq/Documents/IRBA/dev/eulearning")
from descriptor import EulerCharacteristicProfile


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


def _euler_curve(vecs_st, hyperparams):
    euler_curve = EulerCharacteristicProfile(resolution=(200,), quantiles=[(0, 0.95)], pt_cld=True, normalize=False)
    ecc = euler_curve.fit_transform(vecs_st)
    # # Plot Euler curves
    # ecc_range = np.linspace(euler_curve.val_ranges[0][0], euler_curve.val_ranges[0][1], euler_curve.resolution[0])
    return ecc