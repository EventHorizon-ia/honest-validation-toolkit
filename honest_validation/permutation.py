import numpy as np

def permutation_test(y_true, y_pred, n_permutations=100, seed=42):
    rng = np.random.default_rng(seed)
    acc_real = np.mean(y_true == y_pred)
    acc_perm = []
    for _ in range(n_permutations):
        y_perm = rng.permutation(y_true)
        acc_perm.append(np.mean(y_perm == y_pred))
    return acc_real, np.mean(acc_perm), np.percentile(acc_perm, [2.5, 97.5])