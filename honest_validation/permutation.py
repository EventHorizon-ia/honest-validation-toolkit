import numpy as np

def permutation_test(y_true, y_pred, n_permutations=100, seed=42):
    """
    Permutation test for statistical significance.
    
    Parameters
    ----------
    y_true : array-like
        Ground truth labels.
    y_pred : array-like
        Predicted labels.
    n_permutations : int, optional
        Number of permutations (default 100).
    seed : int, optional
        Random seed (default 42).
    
    Returns
    -------
    real_acc : float
        Observed accuracy.
    null_mean : float
        Mean accuracy under the null distribution.
    ci_bounds : ndarray
        [2.5, 97.5] percentiles of the null distribution.
    """
    rng = np.random.default_rng(seed)
    real_acc = np.mean(y_true == y_pred)
    null_accs = []
    for _ in range(n_permutations):
        y_perm = rng.permutation(y_true)
        null_accs.append(np.mean(y_perm == y_pred))
    return real_acc, np.mean(null_accs), np.percentile(null_accs, [2.5, 97.5])