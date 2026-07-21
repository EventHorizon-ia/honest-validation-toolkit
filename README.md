# Event Horizon — AI-Powered Cryptocurrency Prediction System

Artificial intelligence system for predicting cryptocurrency price direction across multiple timeframes using Transformer and BiLSTM architectures (PyTorch).

## 🧠 System Architecture

**Neural Network**
- **Backbone:** 6-block Transformer (8 attention heads) + 2-layer bidirectional LSTM
- **Heads:** 10 specialized prediction heads, one per temporal horizon (5s, 15s, 30s, 1min, 5min, 15min, 30min, 1h, 5h, 1d)
- **Training:** AdamW optimizer with CosineAnnealingWarmRestarts scheduler
- **Gradient Flow:** Full backpropagation through the entire backbone (embedding → Transformer → LSTM → cross-attention → heads)

**Verification Pipeline**
- **Delayed Reward Buffer:** Rewards are only computed when the target horizon actually elapses
- **Statistical Subsampling:** Prevents temporal autocorrelation by enforcing sample independence
- **Public Audit Trail:** Every prediction is verified against real Binance prices and logged publicly
- **Wilson Confidence Intervals:** Statistical significance testing on all accuracy metrics

**Signal Engine**
- Multi-horizon signal evaluation with configurable minimum accuracy thresholds
- Risk/reward calculation based on real-time ATR (Average True Range)
- Confluence detection across temporal groups (micro, scalping, intraday, swing)
- Telegram and Discord integration for automated signal delivery

## 📊 Current Performance

| Metric | Value |
|--------|-------|
| Training Data | 365 days of 1-second Binance candles |
| Training Hardware | Google Colab T4 GPU |
| Final Training Accuracy (avg 5s–1h) | **54.9%** |
| Best Single Horizon | **1h — 59.8%** (stable for 5 consecutive epochs) |
| Second Best Horizon | 15min — 55.4% |
| Verified Against | Real Binance prices, no backtesting, no cherry-picking |
| Audit Panel | Publicly accessible |

*All accuracy metrics were validated on an 80/20 temporal split with no data leakage, confirmed by permutation testing.*

## 🛠 Technology Stack

- **Language:** Python 3
- **Deep Learning:** PyTorch, custom Transformer, custom BiLSTM
- **Frontend:** Next.js, HTML5/CSS3
- **Data Sources:** Binance REST API, local JSON verification store, Supabase
- **Infrastructure:** Custom training pipeline, no AutoML frameworks, no third-party trading libraries

## 🔬 Key Technical Challenges Solved

- **Autocorrelation bias:** Identified and corrected temporal dependency in training samples through subsampling
- **Gradient truncation:** Fixed gradient flow issue where backprop was stopping at prediction heads, not reaching the backbone
- **Reward leakage:** Implemented delayed reward buffer to prevent future information from leaking into training
- **Convergence stagnation:** Replaced static learning rate scheduler with CosineAnnealingWarmRestarts
- **Temporal misalignment:** Debugged and fixed horizon shift bugs that caused artificial accuracy inflation (82.9% fake)

## 🚧 Project Status

**Active development and continuous training.** The system runs 24/7, processing real-time Binance data, training the neural network online, and publishing auditable predictions. Current focus: improving accuracy on longer timeframes (1h, 5h, 1d) as more independent samples accumulate.

## 👤 Author

Developed entirely by Lucas, age 13, Brazil.

Candidate for the ITA Junior Members Program (Sócio Mirins) and OBCIT 3rd Phase.

## 🔗 Links

- **Public Audit Dashboard:** https://eventhorizon-ia.github.io/trader-ai/dashboard-en.html
- **Landing Page:** https://eventhorizon-ia.github.io/trader-ai/index-en.html
- **Technical Article (Dev.to):** [Lessons from Building a Multi-Horizon Crypto Prediction System with Transformers](https://dev.to/eventhorizon-ia)
- **Technical Article (TabNews):** Como um bug de autocorrelação inflou a acurácia do meu modelo em 30% (em português)
