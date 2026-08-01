"""
honest-validation-toolkit
=========================

Lightweight Python library for rigorous time-series validation.

Provides bootstrap confidence intervals, permutation tests, and
walk-forward splitting — all respecting temporal order.

Main functions
--------------
- block_bootstrap : Temporal block bootstrap for accuracy confidence intervals
- gap_bootstrap    : Paired difference bootstrap (real vs. permuted)
- permutation_test : Permutation test for statistical significance
- walkforward_split: Chronological train/validation split
- wape             : Weighted Absolute Percentage Error
- mase             : Mean Absolute Scaled Error

Examples
--------
>>> from honest_validation import block_bootstrap, wape
>>> import numpy as np
>>> y_true = np.array([1, 0, 1, 1, 0])
>>> y_pred = np.array([1, 1, 1, 0, 0])
>>> hits = (y_true == y_pred).astype(int)
>>> ci_low, ci_high = block_bootstrap(hits, block_size=2, n_boot=500)
"""

from .bootstrap import block_bootstrap, gap_bootstrap
from .walkforward import walkforward_split
from .permutation import permutation_test
from .metrics import wape, mase