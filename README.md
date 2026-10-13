# honest-validation-toolkit

> **Lightweight Python library for rigorous time-series validation.**  
> Used across EventHorizon research projects. Available as a standalone package.

![PyPI](https://img.shields.io/pypi/v/honest-validation-toolkit)
![License](https://img.shields.io/github/license/EventHorizon-ia/honest-validation-toolkit)
![Python](https://img.shields.io/pypi/pyversions/honest-validation-toolkit)

---

# Why This Exists

Many forecasting projects report a single accuracy number without showing:

-  Confidence intervals
-  Temporal awareness
-  Protection against autocorrelation-related bias
-  A clear comparison against an appropriate baseline

This library provides validation utilities used across EventHorizon research:

-  Crypto research: investigated short-horizon BTC/USDT directional
  prediction, estimated uncertainty and documented that the evaluated strategy
  was economically unviable.
-  Retail demand research: estimated uncertainty around a WAPE improvement
  over a naive lag-7 baseline using block and paired gap bootstraps.

> **The goal is simple:** make temporal evaluation, uncertainty estimation and
> baseline comparison more explicit, reducing the risk of temporal leakage and
> misleading statistical conclusions.

---

# Features

| Feature | Description |
|---|---|
|  **Framework Agnostic** | Works with NumPy arrays and pandas-compatible outputs; compatible with PyTorch, LightGBM, scikit-learn, XGBoost, CatBoost and custom models. |
|  **Domain Agnostic** | Supports classification and regression workflows. |
|  **Time-Series Aware** | Validation utilities preserve chronological order. |
|  **Statistical Evidence** | Includes bootstrap confidence intervals, gap analysis and permutation-based null comparisons. |
|  **Lightweight** | Core dependencies are NumPy and pandas. |

---

# Installation

```bash
pip install honest-validation-toolkit
```

**Dependencies**

| Package | Required |
|---|---|
| NumPy | ✅ |
| pandas | ✅ |

No deep-learning framework is required.

---

# Quick Start

```python
from honest_validation import block_bootstrap, wape
import numpy as np

# Classification
y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1])
y_pred = np.array([1, 1, 1, 0, 0, 1, 0, 1, 1, 0])

hits = (y_true == y_pred).astype(int)

ci_low, ci_high = block_bootstrap(
    hits,
    block_size=3,
    n_boot=1000,
    seed=42
)

print(f"Accuracy 95% CI: [{ci_low:.2%}, {ci_high:.2%}]")


# Regression
y_true = np.array([100, 120, 90, 110, 130])
y_pred = np.array([105, 115, 95, 105, 125])

error = wape(y_true, y_pred)

print(f"WAPE: {error:.2f}%")
```

---

# Available Functions

| Function | Domain | Purpose |
|---|---|---|
| **block_bootstrap** | Classification | Moving block bootstrap for uncertainty estimation and confidence intervals |
| **gap_bootstrap** | Classification | Bootstrap interval for the difference between a real result and a permuted/null result |
| **permutation_test** | Classification | Approximate permutation test using a target-shuffled null distribution |
| **walkforward_split** | General | Walk-forward temporal split with configurable embargo |
| **wape** | Regression | Weighted Absolute Percentage Error |
| **mase** | Regression | Mean Absolute Scaled Error |

 **Complete documentation:** [GUIDE.md](https://github.com/EventHorizon-ia/honest-validation-toolkit/blob/main/GUIDE.md)

---

# Validation Philosophy

Unlike approaches that randomly shuffle observations, this toolkit treats
time as a first-class citizen.

| Principle | Description |
|---|---|
|  **Temporal Awareness** | Resampling and evaluation utilities preserve chronological structure. |
|  **Honest Intervals** | Report uncertainty alongside point estimates. |
|  **Reference Comparison** | Compare observed results with an appropriate baseline or permutation-based null result. |
|  **Leakage Awareness** | Use temporal splits, embargo and chronological evaluation to reduce leakage risk. |

---

# What This Toolkit Helps Answer

- How uncertain is an estimated performance metric?
- Is an observed improvement distinguishable from an appropriate baseline?
- Does performance remain stable under temporal resampling?
- Does the evaluation respect the chronological structure of the data?
- Is an apparent improvement plausibly explained by randomness or temporal
  dependence?

The output is statistical evidence about model performance.

---

# What This Toolkit Does Not Validate

Statistical validation is only one part of evaluating a real-world forecasting
system.

This toolkit does not determine:

-  Whether a model is economically profitable
-  Whether forecast errors create meaningful business losses
-  Whether a business can operationally act on the predictions
-  Whether the model fits an organization’s existing workflow
-  Whether the model creates sufficient business value to justify adoption

A result that appears statistically distinguishable from a baseline can still
be economically irrelevant.

Likewise, a model can have useful operational value even when a particular
statistical test does not capture every aspect of that value.

> Statistical validity and real-world viability are separate questions.

---



# Typical Workflow

```text
Raw Predictions
        │
        ▼
Temporal / Walk-Forward Split
        │
        ▼
Point Metrics
        │
        ▼
Bootstrap Confidence Intervals
        │
        ▼
Permutation / Paired Gap Analysis
        │
        ▼
Uncertainty and Baseline Comparison
```

---

# Use Cases

-  Financial forecasting
-  Cryptocurrency prediction
-  Retail demand forecasting
-  Energy-consumption forecasting
-  Supply-chain optimization
-  Machine-learning research
-  Forecasting-model benchmarking

---

# Repository Structure

```text
honest-validation-toolkit/
├── honest_validation/
│   ├── __init__.py
│   ├── bootstrap.py
│   ├── walkforward.py
│   ├── permutation.py
│   └── metrics.py
├── GUIDE.md
├── README.md
└── pyproject.toml
```

---

# Links

| Project | Link |
|---|---|
|  EventHorizon-AI Hub | https://github.com/EventHorizon-ia/EventHorizon |
|  Crypto Research | https://github.com/EventHorizon-ia/crypto-h0-edge |
|  Demand Research | https://github.com/EventHorizon-ia/demand-m5 |

---

# License

MIT License.
