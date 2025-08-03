# 🏎️ F1 Qualifying Telemetry Analysis — Hungary GP 2025

This project explores and visualizes driver telemetry data from the **2025 Hungarian Grand Prix Qualifying session** using the [`FastF1`](https://theoehrly.github.io/Fast-F1/) package.

We focus on comparing key telemetry metrics (Speed, Throttle, Brake, RPM, etc.) across selected drivers — **Leclerc (LEC)**, **Norris (NOR)**, and **Piastri (PIA)** — to reveal subtle differences in driving styles and car behavior.

---

## 🧠 Bonus: Podium Prediction Model

In addition to telemetry visualizations, this repository includes a machine learning model trained on **2024 season data** — especially from the **Hungarian Grand Prix (FP1, FP2, FP3, Quali)** — to **predict the podium finishers for the 2025 race**.

- Model type: XGBoost Regressor
- Features used: session pace, tire usage, qualifying positions, team dynamics, and driver form
- Evaluation metric: MAE (Mean Absolute Error)
- Current MAE: ~1.52 (position prediction)

---

## 📦 Technologies & Packages

- Python 3.10+
- [FastF1](https://theoehrly.github.io/Fast-F1/) - For retrieving Formula 1 session data
- `pandas`, `numpy` - Data manipulation
- `xgboost`, `scikit-learn` - ML modeling
- `matplotlib`, `seaborn` - For 2D visualizations
- `plotly` - For interactive and 3D plots
- `umap-learn`, `mplsoccer`, etc. (for dimensionality reduction and radar charts)

---

## 📊 Features

- ✅ Fastest lap telemetry analysis for LEC, NOR, PIA
- ✅ 2D KDE heatmaps (Speed vs Throttle, etc.)
- ✅ Pairplots to compare driver behavior
- ✅ 3D telemetry visualization using Plotly
- ✅ Machine learning model for 2025 podium prediction


---


