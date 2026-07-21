import numpy as np

def block_bootstrap(acertos, block_size=50, n_boot=2000, seed=42):
    rng = np.random.default_rng(seed)
    n = len(acertos)
    n_blocks = n // block_size
    if n_blocks < 2:
        medias = [np.random.choice(acertos, size=n, replace=True).mean() for _ in range(n_boot)]
        return np.percentile(medias, [2.5, 97.5])
    blocos = [acertos[i*block_size:(i+1)*block_size] for i in range(n_blocks)]
    if n % block_size != 0:
        blocos.append(acertos[n_blocks*block_size:])
        n_blocks = len(blocos)
    medias_boot = [np.concatenate([blocos[rng.integers(n_blocks)] for _ in range(n_blocks)]).mean() for _ in range(n_boot)]
    return np.percentile(medias_boot, [2.5, 97.5])

def gap_bootstrap(real, permutado, block_size=30, n_boot=2000, seed=42):
    rng = np.random.default_rng(seed)
    n = min(len(real), len(permutado))
    n_blocks = n // block_size
    if n_blocks < 2:
        return None, None
    n_use = n_blocks * block_size
    real, permutado = real[:n_use], permutado[:n_use]
    blocos_real = [real[i*block_size:(i+1)*block_size] for i in range(n_blocks)]
    blocos_perm = [permutado[i*block_size:(i+1)*block_size] for i in range(n_blocks)]
    gaps = []
    for _ in range(n_boot):
        idx = rng.choice(n_blocks, size=n_blocks, replace=True)
        amostra_real = np.concatenate([blocos_real[i] for i in idx])
        amostra_perm = np.concatenate([blocos_perm[i] for i in idx])
        gaps.append(amostra_real.mean() - amostra_perm.mean())
    return np.percentile(gaps, [2.5, 97.5])