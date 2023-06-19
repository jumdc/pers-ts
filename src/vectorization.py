import sys

import gudhi.representations
import numpy as np
import pyrootutils

sys.path.append("/home/jmordacq/Documents/IRBA/dev/eulearning")

from eulearning.descriptors import EulerCharacteristicProfile, HybridTransform


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
    """
    Compute the Euler curve of a simplex trees

    Parameters
    ----------
    vecs_st : list
        List of vectorized simplex trees
    hyperparams : dict
        Dictionary of hyperparameters
    
    Returns
    -------
    ecc : list
        List of Euler curves
    """
    trf = EulerCharacteristicProfile(
        resolution=hyperparams['resolution'], quantiles=hyperparams['quantiles'], 
        pt_cld=False, normalize=hyperparams['normalize']
    )
    ecc = trf.fit_transform(vecs_st)
    return ecc, trf


def _hybrid_transform(vecs_st, hyperparams):
    """
    Compute the hybrid transform of simplex trees

    Parameters
    ----------
    vecs_st : list
        List of vectorized simplex trees
    hyperparams : dict
        Dictionary of hyperparameters
    """
    kernel = lambda x : np.exp(-x)
    trf = HybridTransform(
        resolution=hyperparams['resolution'], quantiles=hyperparams['quantiles'],
        pt_cld=False, normalize=hyperparams['normalize'], kernel_name=hyperparams['kernel_name']
    )
    ht = trf.fit_transform(vecs_st)
    return ht, trf
 