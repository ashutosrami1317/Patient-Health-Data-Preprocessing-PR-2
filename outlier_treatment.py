"""Part B: Outlier detection with Z-score, IQR, percentile and winsorization."""
import pandas as pd
import numpy as np

df = pd.read_csv("../Dataset/mice_imputed_intermediate.csv")
columns = ["bmi","blood_pressure","cholesterol","glucose"]
rows = []
for col in columns:
    s = df[col].dropna()
    z = ((s-s.mean())/s.std(ddof=0)).abs()
    q1, q3 = s.quantile(.25), s.quantile(.75)
    iqr = q3-q1
    low_iqr, high_iqr = q1-1.5*iqr, q3+1.5*iqr
    p01, p99 = s.quantile(.01), s.quantile(.99)
    rows.append([col, int((z>3).sum()), int(((s<low_iqr)|(s>high_iqr)).sum()),
                 int(((s<p01)|(s>p99)).sum()), p01, p99])
    # Winsorization: cap values at 1st and 99th percentiles
    df[col] = df[col].clip(p01, p99)
pd.DataFrame(rows, columns=["column","z_score_count","iqr_count","percentile_count","p01","p99"]).to_csv("../Reports/Outlier_Detection_Report.csv", index=False)
df.to_csv("../Dataset/cleaned_patient_data.csv", index=False)
print("Outlier report and cleaned dataset saved.")
