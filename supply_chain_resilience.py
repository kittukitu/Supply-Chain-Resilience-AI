import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from datetime import timedelta
import matplotlib.pyplot as plt
import seaborn as sns


# Step 1: Generate synthetic logistics disruption dataset
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", periods=365)


# Simulated features for logistics environment
num_shipments = np.random.poisson(50, size=365)  # daily shipments
weather_risk = np.random.uniform(0, 1, size=365)  # weather risk score 0-1
supplier_reliability = np.random.uniform(0.8, 1.0, size=365)  # supplier reliability (0.8-1.0)
port_congestion = np.random.binomial(1, 0.3, size=365)  # 30% chance of congestion
maintenance_needed = np.random.binomial(1, 0.1, size=365)  # 10% days with maintenance need


# Simulated disruption risk score based on factors
base_risk = 0.2 + weather_risk * 0.4 + (1 - supplier_reliability) * 0.2 + port_congestion * 0.1 + maintenance_needed * 0.1
disruption_risk = base_risk + np.random.normal(0, 0.05, 365)  # add noise
disruption_risk = np.clip(disruption_risk, 0, 1)  # bound between 0 and 1


data = pd.DataFrame({
    'date': dates,
    'num_shipments': num_shipments,
    'weather_risk': weather_risk,
    'supplier_reliability': supplier_reliability,
    'port_congestion': port_congestion,
    'maintenance_needed': maintenance_needed,
    'disruption_risk': disruption_risk
})

# Save generated dataset to CSV
data.to_csv("logistics_disruption_dataset.csv", index=False)
print("Synthetic logistics disruption dataset saved as 'logistics_disruption_dataset.csv'.")


# Step 2: Feature engineering (lag features, rolling averages)
for lag in [1, 2, 3, 7]:
    data[f'disruption_risk_lag{lag}'] = data['disruption_risk'].shift(lag).bfill()
data['rolling_avg7'] = data['disruption_risk'].rolling(7, min_periods=1).mean()


features = ['num_shipments', 'weather_risk', 'supplier_reliability', 'port_congestion',
            'maintenance_needed', 'disruption_risk_lag1', 'disruption_risk_lag2',
            'disruption_risk_lag3', 'disruption_risk_lag7', 'rolling_avg7']
target = 'disruption_risk'


# Step 3: Train/test split (no shuffle for time series)
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.1, shuffle=False)


# Step 4: Train XGBoost model
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)


# Step 5: Evaluate model performance
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Test RMSE: {rmse:.3f}")


# Step 6: User input for next-day risk prediction
print("\nEnter values for next-day prediction:")
sample = {}


for f in features:
    if 'lag' in f or f == 'rolling_avg7':
        sample[f] = float(data[f].iloc[-1])
    else:
        val = input(f"{f} (e.g. {data[f].iloc[-1]:.3f}): ")
        sample[f] = float(val) if '.' in val else int(val)


user_df = pd.DataFrame([sample])
user_pred = model.predict(user_df)[0]
print(f"\nPredicted Disruption Risk for next day: {user_pred:.3f}")


# Step 6b: Basic recommendations based on predicted risk
print("\nRecommendations:")
if user_pred > 0.7:
    print("- High risk of disruption: consider rerouting shipments or increasing inventory buffers.")
elif user_pred > 0.4:
    print("- Moderate risk detected: monitor logistics closely and inspect equipment status.")
else:
    print("- Low disruption risk: maintain current operations.")


if sample['maintenance_needed'] == 1:
    print("- Schedule preventive maintenance to reduce downtime risk.")


if sample['port_congestion'] == 1:
    print("- Coordinate with port authorities for alternative processing slots.")


# Step 7: Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(x='date', y='disruption_risk', data=data, label='Actual Disruption Risk')
plt.scatter([data['date'].iloc[-1] + timedelta(days=1)], [user_pred], color='red', label='Prediction')
plt.title('Logistics Disruption Risk Forecast & User Prediction')
plt.xlabel('Date')
plt.ylabel('Disruption Risk')
plt.legend()
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,7))
sns.heatmap(data[features + [target]].corr(), annot=True, cmap='YlGnBu')
plt.title('Feature Correlation Heatmap')
plt.show()
