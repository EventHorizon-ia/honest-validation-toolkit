import numpy as np

def block_bootstrap(hits, block_size=50, n_boot=2000, seed=42):
    """
    Temporal block bootstrap for classification accuracy confidence intervals.
    
    Parameters
    ----------
    hits : array-like of int (0 or 1)
        Binary array indicating correct (1) or incorrect (0) predictions.
    block_size : int, optional
        Size of temporal blocks for resampling (default 50).
    n_boot : int, optional
        Number of bootstrap iterations (default 2000).
    seed : int, optional
        Random seed for reproducibility (default 42).
    
    Returns
    -------
    ci_low : float
        Lower bound of the 95% confidence interval.
    ci_high : float
        Upper bound of the 95% confidence interval.
    """
    rng = np.random.default_rng(seed)
    n = len(hits)
    n_blocks = n // block_size
    if n_blocks < 2:
        means = [np.random.choice(hits, size=n, replace=True).mean() for _ in range(n_boot)]
        return np.percentile(means, [2.5, 97.5])
    blocks = [hits[i*block_size:(i+1)*block_size] for i in range(n_blocks)]
    if n % block_size != 0:
        blocks.append(hits[n_blocks*block_size:])
        n_blocks = len(blocks)
    boot_means = [np.concatenate([blocks[rng.integers(n_blocks)] for _ in range(n_blocks)]).mean() for _ in range(n_boot)]
    return np.percentile(boot_means, [2.5, 97.5])


def gap_bootstrap(real, permuted, block_size=30, n_boot=2000, seed=42):
    """
    Paired difference bootstrap comparing real vs. permuted accuracies.
    
    Parameters
    ----------
    real : array-like of float
        Real accuracy values.
    permuted : array-like of float
        Permuted accuracy values (same length as real).
    block_size : int, optional
        Size of temporal blocks (default 30).
    n_boot : int, optional
        Number of bootstrap iterations (default 2000).
    seed : int, optional
        Random seed (default 42).
    
    Returns
    -------
    ci_low : float or None
        Lower bound of the 95% CI (None if insufficient data).
    ci_high : float or None
        Upper bound of the 95% CI (None if insufficient data).
    """
    rng = np.random.default_rng(seed)
    n = min(len(real), len(permuted))
    n_blocks = n // block_size
    if n_blocks < 2:
        return None, None
    n_use = n_blocks * block_size
    real, permuted = real[:n_use], permuted[:n_use]
    blocks_real = [real[i*block_size:(i+1)*block_size] for i in range(n_blocks)]
    blocks_perm = [permuted[i*block_size:(i+1)*block_size] for i in range(n_blocks)]
    gaps = []
    for _ in range(n_boot):
        idx = rng.choice(n_blocks, size=n_blocks, replace=True)
        sample_real = np.concatenate([blocks_real[i] for i in idx])
        sample_perm = np.concatenate([blocks_perm[i] for i in idx])
        gaps.append(sample_real.mean() - sample_perm.mean())
    return np.percentile(gaps, [2.5, 97.5])