""" Scan outlier metrics
"""

# Any imports you need
import numpy as np

def dvars(img):
    """ Calculate dvars metric on Nibabel image `img`

    The dvars calculation between two volumes is defined as the square root of
    (the mean of the (voxel differences squared)).

    Parameters
    ----------
    img : nibabel image

    Returns
    -------
    dvals : 1D array
        One-dimensional array with n-1 elements, where n is the number of
        volumes in `img`.
    """
    data = img.get_fdata()
    data_2d = data.reshape(-1, data.shape[-1])
    dvals = np.sqrt(np.mean(np.square(np.diff(data_2d, axis=1)), axis=0))
    return dvals
