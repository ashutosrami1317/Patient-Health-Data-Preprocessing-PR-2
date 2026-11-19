"""Generate a synthetic Patient Health Records dataset (educational use only)."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 5000
age = rng.integers(18, 86, n)
gender = rng.choice(["Male", "Female", "Other"], n, p=[0.49, 0.49, 0.02])
region = rng.choice(["North", "South", "East", "West"], n)
bmi = np.clip(rng.normal(26.5, 5.2, n), 15, 48)
blood_pressure = np.clip(rng.normal(122, 17, n), 80, 190)
cholesterol = np.clip(rng.normal(195, 38, n), 110, 320)
glucose = np.clip(rng.normal(103, 24, n), 60, 220)
risk_score = (0.025*(age-45) + 0.12*(bmi-25) + 0.018*(blood_pressure-120)
              + 0.012*(cholesterol-190) + 0.035*(glucose-100) + rng.normal(0, 2, n))
disease_risk = (risk_score > np.quantile(risk_score, 0.58)).astype(int)
data = pd.DataFrame({
    "patient_id": np.arange(100001, 100001+n), "age": age, "gender": gender,
    "region": region, "bmi": bmi.round(1), "blood_pressure": blood_pressure.round(1),
    "cholesterol": cholesterol.round(1), "glucose": glucose.round(1),
    "disease_risk": disease_risk
})
for col, count, low, high in [
    ("bmi",55,52,75),("blood_pressure",60,205,260),
    ("cholesterol",55,340,480),("glucose",60,240,390)
]:
    idx = rng.choice(n, count, replace=False)
    data.loc[idx, col] = rng.uniform(low, high, count).round(1)
for col, rate in {"age":.045,"gender":.035,"region":.04,"bmi":.06,"cholesterol":.055,"glucose":.05}.items():
    idx = rng.choice(n, int(n*rate), replace=False)
    data.loc[idx, col] = np.nan
data.to_csv("../Dataset/raw_patient_data.csv", index=False)
print("Created 5,000 synthetic records.")
