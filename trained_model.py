import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load datasets
telemetry = pd.read_csv("dataset/PdM_telemetry.csv")
failures = pd.read_csv("dataset/PdM_failures.csv")

# Create temperature column
telemetry['temperature'] = telemetry['volt'] * 0.5

# Create failure labels
telemetry['failure'] = 0

failure_ids = failures['machineID'].unique()

telemetry.loc[
    telemetry['machineID'].isin(failure_ids),
    'failure'
] = 1

# Features
X = telemetry[['temperature',
               'pressure',
               'rotate',
               'vibration']]

# Target
y = telemetry['failure']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully")