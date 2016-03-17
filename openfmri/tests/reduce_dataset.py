#!/usr/bin/env python
""" Process openfmri dataset in-place replacing large scans with tiny ones

Also, delete any ``dwi`` or ``QA`` subdirectories.

Requires numpy and nibabel
"""

from __future__ import print_function

import os
import sys
from os.path import join as pjoin


TEMPLATE_SHAPE = (4, 5, 6, 2)



def main():
    import numpy as np
    import nibabel as nib
    nib.volumeutils.default_compresslevel = 9

    root = sys.argv[1] if len(sys.argv) > 1 else '.'

    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if not fname.endswith('.nii.gz'):
                continue
            fpath = pjoin(dirpath, fname)
            img = nib.load(fpath)
            shape = TEMPLATE_SHAPE[:len(img.shape)]
            img = nib.Nifti1Image(np.zeros(shape), img.affine, img.header)
            print('Saving', fpath)
            nib.save(img, fpath)
        pruned = []
        for dirname in dirnames:
            if dirname in ('dwi', 'QA'):
                os.removedirs(pjoin(dirpath, dirname))
            else:
                pruned.append(dirname)
        dirnames[:] = pruned


if __name__ == '__main__':
    main()
