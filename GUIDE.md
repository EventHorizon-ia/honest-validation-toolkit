# honest-validation-toolkit — Complete Guide

> **Comprehensive documentation for every function in the library.**  
> Includes API reference, practical examples, implementation notes and best practices for statistically rigorous time-series validation.

---

# Table of Contents

| Section | Description |
|---------|-------------|
| [`block_bootstrap`](#block_bootstrap) | Confidence intervals for classification accuracy |
| [`gap_bootstrap`](#gap_bootstrap) | Bootstrap comparison against a baseline |
| [`permutation_test`](#permutation_test) | Statistical significance testing |
| [`walkforward_split`](#walkforward_split) | Chronological train/validation split |
| [`wape`](#wape) | Weighted Absolute Percentage Error |
| [`mase`](#mase) | Mean Absolute Scaled Error |
| [Complete Example](#complete-example) | End-to-end usage |
| [Framework Compatibility](#framework-compatibility) | Supported ML frameworks |

---

# block_bootstrap

Estimate a **95% confidence interval** for classification accuracy using a **temporal block bootstrap**.

Unlike standard bootstrap, consecutive observations remain grouped into blocks, preserving temporal dependence.

---

## Function Signature

```python
block_bootstrap(
    hits,
    block_size=50,
    n_boot=2000,
    seed=42
)
```

---

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **hits** | array-like[int] | — | Binary vector (1 = correct prediction, 0 = incorrect) |
| **block_size** | int | 50 | Number of consecutive observations per block |
| **n_boot** | int | 2000 | Number of bootstrap resamples |
| **seed** | int | 42 | Random seed |

---

## Returns

| Return | Type | Description |
|---------|------|-------------|
| **ci_low** | float | Lower 95% confidence bound |
| **ci_high** | float | Upper 95% confidence bound |

---

## Example

```python
import numpy as np
from honest_validation import block_bootstrap

y_true = np.array([
    1,0,1,1,0,1,0,0,1,1,
    0,1,0,1,0,0,1,1,0,1
])

y_pred = np.array([
    1,1,1,0,0,1,0,1,1,0,
    0,1,0,0,0,1,1,1,0,1
])

hits = (y_true == y_pred).astype(int)

ci_low, ci_high = block_bootstrap(
    hits,
    block_size=3,
    n_boot=2000
)

print(f"Accuracy: {hits.mean():.2%}")
print(f"95% CI: [{ci_low:.2%}, {ci_high:.2%}]")
```

---

## Notes

- Falls back to standard bootstrap if fewer than two complete blocks exist.
- Larger blocks preserve more temporal dependence but increase interval width.
- Compatible with every ML framework.

---

# gap_bootstrap

Compare a model against a baseline using **paired temporal bootstrap**.

Useful for measuring whether a model truly improves over another while preserving temporal dependence.

---

## Function Signature

```python
gap_bootstrap(
    real,
    permuted,
    block_size=30,
    n_boot=2000,
    seed=42
)
```

---

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **real** | array-like | — | Accuracy from the real model |
| **permuted** | array-like | — | Accuracy from the baseline/permuted model |
| **block_size** | int | 30 | Temporal block length |
| **n_boot** | int | 2000 | Bootstrap iterations |
| **seed** | int | 42 | Random seed |

---

## Returns

| Return | Type | Description |
|---------|------|-------------|
| **ci_low** | float or None | Lower confidence bound |
| **ci_high** | float or None | Upper confidence bound |

---

## Example

```python
import numpy as np
from honest_validation import gap_bootstrap

real_acc = np.array([1,1,0,1,1,0,1,0,1,1], dtype=float)

rng = np.random.default_rng(123)
baseline = rng.permutation(real_acc)

ci_low, ci_high = gap_bootstrap(
    real_acc,
    baseline,
    block_size=3
)

print(ci_low, ci_high)
```

---

## Interpretation

| Result | Meaning |
|---------|---------|
| CI entirely above zero | Model significantly outperforms baseline |
| CI crosses zero | No statistical evidence of improvement |
| Returns `None` | Too little data |

---

# permutation_test

Permutation-based significance test comparing observed accuracy against the null distribution.

---

## Function Signature

```python
permutation_test(
    y_true,
    y_pred,
    n_permutations=100,
    seed=42
)
```

---

## Parameters

| Parameter | Type | Default |
|-----------|------|---------|
| **y_true** | array-like | — |
| **y_pred** | array-like | — |
| **n_permutations** | int | 100 |
| **seed** | int | 42 |

---

## Returns

| Return | Description |
|---------|-------------|
| **real_acc** | Observed accuracy |
| **null_mean** | Mean null accuracy |
| **ci_bounds** | 95% confidence interval of null distribution |

---

## Example

```python
real_acc, null_mean, ci = permutation_test(
    y_true,
    y_pred,
    n_permutations=1000
)

print(real_acc)
print(null_mean)
print(ci)
```

---

## Interpretation

| Result | Meaning |
|---------|---------|
| Real accuracy > upper CI | Statistically significant |
| Real accuracy inside CI | Cannot reject the null hypothesis |

---

# walkforward_split

Chronological train/validation split with optional embargo.

Perfect for production-like validation.

---

## Function Signature

```python
walkforward_split(
    df,
    train_until,
    val_start,
    embargo=0
)
```

---

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| **df** | DataFrame | Time-indexed dataset |
| **train_until** | datetime or str | Last training date |
| **val_start** | datetime or str | First validation date |
| **embargo** | int | Gap (days) between train and validation |

---

## Returns

| Return | Description |
|---------|-------------|
| **train** | Training DataFrame |
| **val** | Validation DataFrame |

---

## Example

```python
import pandas as pd

dates = pd.date_range("2024-01-01", periods=100)

df = pd.DataFrame(
    {"value": range(100)},
    index=dates
)

train, val = walkforward_split(
    df,
    "2024-03-01",
    "2024-03-08",
    embargo=7
)
```

---

## Notes

- Index must be datetime.
- Embargo helps avoid temporal leakage.
- Designed for walk-forward backtesting.

---

# wape

Weighted Absolute Percentage Error.

A robust metric for demand forecasting that scales errors by total demand.

---

## Function Signature

```python
wape(
    y_true,
    y_pred
)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| **y_true** | Ground truth values |
| **y_pred** | Predicted values |

---

## Returns

| Type | Description |
|------|-------------|
| float | WAPE (%) |

---

## Formula

```text
WAPE =
Σ |y_true − y_pred|
──────────────────── × 100
    Σ |y_true|
```

---

## Example

```python
error = wape(
    y_true,
    y_pred
)

print(error)
```

---

## Notes

- Handles zero values safely.
- Lower values indicate better models.
- Widely used in retail forecasting.

---

# mase

Mean Absolute Scaled Error.

Compares model error against a seasonal naive baseline.

---

## Function Signature

```python
mase(
    y_true,
    y_pred,
    y_train,
    seasonality=1
)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| **y_true** | Validation values |
| **y_pred** | Model predictions |
| **y_train** | Historical training series |
| **seasonality** | Seasonal period |

---

## Returns

| Type | Description |
|------|-------------|
| float | MASE score |

---

## Formula

```text
MASE =

      MAE(model)
────────────────────
MAE(seasonal naive)
```

---

## Interpretation

| MASE | Meaning |
|------|---------|
| < 1 | Better than naive baseline |
| = 1 | Similar performance |
| > 1 | Worse than naive baseline |

---

# Complete Example

```python
import numpy as np
import pandas as pd

from honest_validation import (
    block_bootstrap,
    gap_bootstrap,
    permutation_test,
    walkforward_split,
    wape,
    mase
)

# ===== Classification =====

y_true = np.array([1,0,1,1,0,1,0,0,1,1])
y_pred = np.array([1,1,1,0,0,1,0,1,1,0])

hits = (y_true == y_pred).astype(int)

ci = block_bootstrap(hits)

real_acc, null_mean, null_ci = permutation_test(
    y_true,
    y_pred
)

# ===== Regression =====

y_true_reg = np.array([100,120,90,110,130])
y_pred_reg = np.array([105,115,95,105,125])

print(wape(y_true_reg, y_pred_reg))

# ===== Walk Forward =====

df = pd.DataFrame(
    {"value": range(30)},
    index=pd.date_range(
        "2024-01-01",
        periods=30
    )
)

train, val = walkforward_split(
    df,
    "2024-01-20",
    "2024-01-22",
    embargo=1
)
```

---

# Framework Compatibility

All functions accept NumPy arrays or pandas objects.

| Framework | Usage |
|-----------|-------|
| ✅ scikit-learn | `model.predict(X)` |
| ✅ LightGBM | `model.predict(X)` |
| ✅ PyTorch | `.detach().cpu().numpy()` |
| ✅ TensorFlow | `.numpy()` |
| ✅ XGBoost | `model.predict(X)` |
| ✅ CatBoost | `model.predict(X)` |
| ✅ Custom Models | Any NumPy-compatible output |

---

# Best Practices

| Recommendation | Reason |
|---------------|--------|
| Prefer walk-forward validation | Mimics production deployment |
| Always report confidence intervals | Point estimates alone are misleading |
| Preserve temporal ordering | Prevents information leakage |
| Use permutation tests | Validate statistical significance |
| Compare against a baseline | Raw accuracy alone has little meaning |

---

# Links

| Resource | Link |
|---------|------|
| 📦 PyPI | [pypi.org/project/honest-validation-toolkit](https://pypi.org/project/honest-validation-toolkit/) |
| 💻 GitHub | [github.com/EventHorizon-ia/honest-validation-toolkit](https://github.com/EventHorizon-ia/honest-validation-toolkit) |
| 🚀 EventHorizon-AI | [github.com/EventHorizon-ia](https://github.com/EventHorizon-ia) |

---

# License

MIT License.
