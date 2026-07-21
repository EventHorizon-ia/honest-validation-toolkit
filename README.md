# honest-validation-toolkit

> **Lightweight Python library for rigorous time-series validation.**  
> Used across all **EventHorizon** products. Now available as a standalone package.

---

# Why This Exists

Most forecasting projects report a single accuracy number with **no confidence interval**, **no temporal awareness**, and **no protection against autocorrelation bias**.

This library provides the same validation pipeline that:

- 📈 Discovered a real **8 percentage point edge** in cryptocurrency prediction (and demonstrated that it was **not economically viable**).
- 📦 Confirmed a **30% improvement** in demand forecasting.

The goal is simple:

> **Measure model performance honestly, without introducing temporal leakage or misleading statistics.**

---

# Features

| Feature | Description |
|---------|-------------|
| ✅ Framework Agnostic | Compatible with **PyTorch**, **LightGBM**, **scikit-learn**, XGBoost, CatBoost and any other framework. |
| 📊 Domain Agnostic | Supports both **classification** and **regression** problems. |
| ⏳ Time-Series Aware | All validation methods respect temporal order. |
| 📈 Statistical Validation | Confidence intervals, bootstrap and permutation tests included. |
| ⚡ Lightweight | Depends only on **NumPy** and **pandas**. |

---

# Installation

```bash
pip install honest-validation-toolkit
```

At the moment, you can also copy the `honest_validation/` folder directly into your project.

---

# Available Functions

| Function | Domain | Purpose |
|----------|--------|---------|
| **block_bootstrap** | Classification | Temporal block bootstrap for accuracy confidence intervals |
| **gap_bootstrap** | Classification | Paired difference bootstrap (real vs. permuted) |
| **wape_bootstrap_por_data** | Regression | Block bootstrap for WAPE while preserving cross-sectional correlation |
| **wape_diff_bootstrap_por_data** | Regression | Paired bootstrap comparing model vs. baseline WAPE |
| **walkforward_split** | General | Walk-forward temporal split with configurable embargo |
| **permutation_test** | Classification | Permutation significance test against the null distribution |
| **wape** | Regression | Weighted Absolute Percentage Error |
| **mase** | Regression | Mean Absolute Scaled Error |

---

# Quick Example

```python
from honest_validation import block_bootstrap, wape

# Classification
ci_low, ci_high = block_bootstrap(
    acertos,
    block_size=50,
    n_boot=2000
)

# Regression
erro = wape(y_true, y_pred)
```

---

# Repository Structure

```text
honest-validation-toolkit/
│
├── honest_validation/
│   ├── __init__.py          # Public API
│   ├── bootstrap.py         # Block and gap bootstrap
│   ├── walkforward.py       # Temporal split with embargo
│   ├── permutation.py       # Permutation testing
│   └── metrics.py           # WAPE, MASE
│
└── README.md
```

---

# Philosophy

| Principle | Description |
|-----------|-------------|
| ⏳ **Temporal Awareness** | Every resampling strategy preserves chronological order. No random shuffling across time. |
| 📊 **Honest Intervals** | Report confidence intervals instead of only point estimates. |
| 🔬 **Statistical Rigor** | Built around bootstrap and permutation methods designed for time-series data. |
| ⚡ **Minimal Dependencies** | Only **NumPy** and **pandas** are required. No framework lock-in. |

---

# Use Cases

- Cryptocurrency forecasting
- Financial time series
- Demand forecasting
- Energy forecasting
- Sales prediction
- Machine learning benchmarking
- Academic research
- Production model validation

---

# Links

| Project | 
|---------|
| 🚀 [EventHorizon-AI hub](https://github.com/EventHorizon-ia/eventhorizon) |
| 📈 [Crypto Research](https://github.com/EventHorizon-ia/crypto-h0-edge) |
| 📦 [Demand Research](https://github.com/EventHorizon-ia/demand-m5) |

---

## License

MIT License.
