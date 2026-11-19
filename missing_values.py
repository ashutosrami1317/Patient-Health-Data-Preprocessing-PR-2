"""Part A: Missing-value analysis and five imputation approaches."""
import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer  # noqa: F401
from sklearn.impute import IterativeImputer

df = pd.read_csv("../Dataset/raw_patient_data.csv")
numeric = ["age","bmi","blood_pressure","cholesterol","glucose"]
categorical = ["gender","region"]
print("Missing summary (%):")
print((df.isna().mean()*100).round(2))

# 1. Simple Imputer: median numeric + most-frequent categorical
simple_df = df.copy()
simple_df[numeric] = SimpleImputer(strategy="median").fit_transform(simple_df[numeric])
simple_df[categorical] = SimpleImputer(strategy="most_frequent").fit_transform(simple_df[categorical])

# 2. Most-frequent imputation (categorical columns)
most_frequent_df = df.copy()
most_frequent_df[categorical] = SimpleImputer(strategy="most_frequent").fit_transform(most_frequent_df[categorical])

# 3. Missing indicator + random-sample imputation
random_df = df.copy()
for col in numeric + categorical:
    missing = random_df[col].isna()
    random_df[col + "_was_missing"] = missing.astype(int)
    observed = random_df.loc[~missing, col].dropna().to_numpy()
    random_df.loc[missing, col] = __import__("numpy").random.default_rng(42).choice(observed, missing.sum(), replace=True)

# 4. KNN numeric; most-frequent categorical
knn_df = df.copy()
knn_df[numeric] = KNNImputer(n_neighbors=5, weights="distance").fit_transform(knn_df[numeric])
knn_df[categorical] = SimpleImputer(strategy="most_frequent").fit_transform(knn_df[categorical])

# 5. MICE / IterativeImputer numeric; most-frequent categorical
mice_df = df.copy()
mice_df[numeric] = IterativeImputer(random_state=42, max_iter=10).fit_transform(mice_df[numeric])
mice_df[categorical] = SimpleImputer(strategy="most_frequent").fit_transform(mice_df[categorical])

print("Missing values after MICE:", int(mice_df.isna().sum().sum()))
mice_df.to_csv("../Dataset/mice_imputed_intermediate.csv", index=False)
