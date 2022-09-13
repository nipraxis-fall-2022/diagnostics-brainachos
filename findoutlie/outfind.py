""" Module with routines for finding outliers
"""

from pathlib import Path

import numpy as np

import nibabel as nib

from .metrics import dvars
from .detectors import iqr_detector


def detect_outliers(fname):
    """ Detect outliers given image file path `filename`

    Parameters
    ----------
    fname : str or Path
        Filename of 4D image, as string or Path object

    Returns
    -------
    outliers : array
        Indices of outlier volumes.
    """
    # This is a very simple function, using dvars and iqroutliers
    img = nib.load(fname)
    dvs = dvars(img)
    is_outlier = iqr_detector(dvs, iqr_proportion=2)
    # Return indices of True values from Boolean array.
    return np.nonzero(is_outlier)


def find_outliers(data_directory):
    """ Return filenames and outlier indices for images in `data_directory`.

    Parameters
    ----------
    data_directory : str
        Directory containing containing images.

    Returns
    -------
    outlier_dict : dict
        Dictionary with keys being filenames and values being lists of outliers
        for filename.
    """
    image_fnames = Path(data_directory).glob('**/sub-*.nii.gz')
    outlier_dict = {}
    for fname in image_fnames:
        outliers = detect_outliers(fname)
        outlier_dict[fname] = outliers
    return outlier_dict
