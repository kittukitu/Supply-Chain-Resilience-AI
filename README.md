Logistics Disruption Risk Prediction
This project generates a synthetic logistics disruption dataset, extracts predictive features, builds a next-day disruption risk prediction model using XGBoost, and provides actionable recommendations and visualizations.

Features
Synthetic daily logistics disruption risk data for one year.

Predictive factors: shipment volume, weather risk, supplier reliability, port congestion, maintenance needs.

Feature engineering: lagged values and rolling risk average.

Time-series compatible train/test split and XGBoost regression modeling.

Interactive next-day prediction using user input.

Actionable recommendations based on predicted risk.

Visualizations: disruption risk forecast and feature correlation heatmap.

Requirements
Python 3.x

pandas

numpy

xgboost

scikit-learn

matplotlib

seaborn

Install dependencies via pip:

bash
pip install pandas numpy xgboost scikit-learn matplotlib seaborn
Usage
Run the script
The script creates a synthetic dataset (logistics_disruption_dataset.csv), trains an XGBoost model, and evaluates its performance.

Next-Day Prediction
When prompted, enter values for the following features for next-day prediction:

num_shipments (integer, daily shipment count)

weather_risk (float, 0–1)

supplier_reliability (float, 0.8–1.0)

port_congestion (0 or 1)

maintenance_needed (0 or 1)

Lag and rolling features auto-filled from latest day

Output

Displays predicted disruption risk for the next day

Provides tailored recommendations:

High risk: rerouting, buffer inventory

Moderate risk: monitor logistics, inspect equipment

Low risk: maintain operations

Additional suggestions for maintenance or congestion

Visualizations

Disruption risk forecast trend, with user prediction marked

Feature correlation heatmap for model interpretability

Files
logistics_disruption_dataset.csv: Generated synthetic logistics data

Script file: Contains all code for data generation, modeling, and visualization

Notes
Lag/rolling features (disruption_risk_lag1, etc.) and rolling_avg7 auto-fill from last known values.

The model is trained/tested without data shuffle to preserve time-series continuity.

Visualizations require a graphical environment to display.