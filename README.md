# honest-validation-toolkit

> **Lightweight Python library for rigorous time-series validation.**  
> Used across all **EventHorizon** products. Now available as a standalone package.

![PyPI](https://img.shields.io/pypi/v/honest-validation-toolkit)
![License](https://img.shields.io/github/license/EventHorizon-ia/honest-validation-toolkit)
![Python](https://img.shields.io/pypi/pyversions/honest-validation-toolkit)

---

# Why This Exists

Most forecasting projects report a single accuracy number with:

- ❌ No confidence interval
- ❌ No temporal awareness
- ❌ No protection against autocorrelation bias

This library provides the same validation pipeline that:

- 📈 Identified a real **8 percentage point predictive edge** in cryptocurrency forecasting (and demonstrated that it was **not economically viable**).
- 📦 Confirmed a **30% improvement** in retail demand forecasting.

> **The goal is simple:** evaluate forecasting models honestly, without temporal leakage or misleading statistical conclusions.

---

# Features

| Feature | Description |
|---------|-------------|
| ✅ **Framework Agnostic** | Compatible with **PyTorch**, **LightGBM**, **scikit-learn**, XGBoost, CatBoost and any custom model. |
| 📊 **Domain Agnostic** | Supports both **classification** and **regression** tasks. |
| ⏳ **Time-Series Aware** | Every validation method preserves chronological order. |
| 📈 **Statistical Validation** | Confidence intervals, bootstrap methods and permutation tests included. |
| ⚡ **Lightweight** | Depends only on **NumPy** and **pandas**. |

---

# Installation

```bash
pip install honest-validation-toolkit
```

**Dependencies**

| Package | Required |
|---------|----------|
| NumPy | ✅ |
| pandas | ✅ |

No deep learning framework is required.

---

# Quick Start

```python
from honest_validation import block_bootstrap, wape
import numpy as np

# Classification
hits = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1])

ci_low, ci_high = block_bootstrap(
    hits,
    block_size=3,
    n_boot=1000
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
|----------|--------|---------|
| **block_bootstrap** | Classification | Temporal block bootstrap for confidence intervals |
| **gap_bootstrap** | Classification | Paired difference bootstrap (real vs. permuted) |
| **permutation_test** | Classification | Statistical significance test against the null distribution |
| **walkforward_split** | General | Walk-forward temporal split with configurable embargo |
| **wape** | Regression | Weighted Absolute Percentage Error |
| **mase** | Regression | Mean Absolute Scaled Error |

📖 **Complete documentation:** [GUIDE.md](https://github.com/EventHorizon-ia/honest-validation-toolkit/blob/main/GUIDE.md)

---

# Validation Philosophy

Unlike traditional validation approaches that randomly shuffle observations, **honest-validation-toolkit** treats time as a first-class citizen.

| Principle | Description |
|-----------|-------------|
| ⏳ **Temporal Awareness** | Every resampling strategy preserves chronological order. |
| 📊 **Honest Intervals** | Report confidence intervals instead of only point estimates. |
| 🔬 **Statistical Rigor** | Bootstrap and permutation methods designed specifically for time-series data. |
| 🚫 **No Data Leakage** | Evaluation follows production conditions as closely as possible. |

---

# What This Toolkit Validates

The toolkit is designed to help answer questions such as:

- Is the observed performance statistically distinguishable from a baseline or null hypothesis?
- How uncertain is the estimated performance?
- Does the result remain stable under temporal resampling?
- Does the evaluation respect the chronological structure of the data?
- Is an apparent improvement likely to be explained by randomness or temporal dependence?

The output is statistical evidence about model performance.

# What This Toolkit Does Not Validate

Statistical validation is only one part of evaluating a real-world forecasting system.

This toolkit does not determine:

- 💰 Whether a model is economically profitable
- 📦 Whether forecast errors create meaningful business losses
- ⚙️ Whether a business can operationally act on the predictions
- 🔄 Whether the model fits an organization's existing workflow
- 📈 Whether the model creates sufficient business value to justify adoption

A statistically significant improvement can still be economically irrelevant.

Likewise, a model can have useful operational value even when a particular statistical test does not capture every aspect of that value.

> Statistical validity and real-world viability are separate questions.


# Typical Workflow

```text
Raw Predictions
        │
        ▼
Walk-Forward Split
        │
        ▼
Bootstrap Confidence Intervals
        │
        ▼
Permutation / Gap Tests
        │
        ▼
Statistically Validated Results
```

---

# Use Cases

- 📈 Financial forecasting
- 🪙 Cryptocurrency prediction
- 🛒 Retail demand forecasting
- ⚡ Energy consumption forecasting
- 📦 Supply chain optimization
- 🎓 Academic machine learning research
- 🤖 Benchmarking forecasting models

---

# Repository Structure

```text
honest-validation-toolkit/
│
├── honest_validation/
│   ├── __init__.py
│   ├── bootstrap.py
│   ├── walkforward.py
│   ├── permutation.py
│   └── metrics.py
│
├── GUIDE.md
├── README.md
└── pyproject.toml
```

---

# Links

| Project | Link |
|---------|------|
| 🚀 EventHorizon-AI Hub | *(https://github.com/EventHorizon-ia/EventHorizon)* |
| 📈 Crypto Research | *(https://github.com/EventHorizon-ia/crypto-h0-edge)* |
| 📦 Demand Research | *(https://github.com/EventHorizon-ia/demand-m5)* |

---

# License

MIT License.
