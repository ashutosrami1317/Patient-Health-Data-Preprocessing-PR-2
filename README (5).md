<div align="center">

# 🏥 Patient Health Data Preprocessing & Feature Engineering

### A Complete Data Cleaning Project Using Python, Pandas & Scikit-learn

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?logo=pandas&logoColor=white)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-Machine_Learning-F7931E?logo=scikitlearn&logoColor=white)
![Project](https://img.shields.io/badge/Project-Educational-success)
![Records](https://img.shields.io/badge/Records-5%2C000-brightgreen)

**Author: Rami Ashutos**

</div>

---

## 📌 Project Overview

This project demonstrates an end-to-end data preprocessing workflow using a **synthetic Patient Health Records dataset containing 5,000 records**.

The main focus is to identify and handle missing values, detect and treat outliers, compare data quality before and after cleaning, and export a final dataset that can be used for further educational machine-learning exercises.

The project follows the three parts of the assignment:

- **Part A:** Handling Missing Values
- **Part B:** Handling Outliers
- **Part C:** Final Clean Dataset and Report

> ⚠️ **Important:** This project uses artificially generated data for educational purposes only. It does not contain real patient information and must not be used for medical diagnosis, treatment, or clinical decisions.

---

## 🎯 Project Objectives

- Understand and inspect a structured health-record dataset.
- Identify missing values and calculate their percentages.
- Apply different missing-value imputation techniques.
- Detect potential outliers using statistical methods.
- Treat extreme values using Winsorization.
- Compare the dataset before and after preprocessing.
- Export a clean dataset and supporting reports.
- Practice organizing a complete Python project for GitHub.

---

## 🗂️ Dataset Information

The raw dataset contains **5,000 synthetic patient records** and the following columns:

| Column Name | Data Type | Description |
|---|---|---|
| `patient_id` | Integer | Unique synthetic patient ID |
| `age` | Numeric | Patient age in years |
| `gender` | Categorical | Male, Female, or Other |
| `region` | Categorical | North, South, East, or West |
| `bmi` | Float | Synthetic Body Mass Index value |
| `blood_pressure` | Float | Synthetic blood pressure measurement |
| `cholesterol` | Float | Synthetic cholesterol measurement |
| `glucose` | Float | Synthetic glucose measurement |
| `disease_risk` | Binary | `0` = Low Risk, `1` = High Risk |

### Missing Values Introduced

Missing values are intentionally added to these columns:

- `age`
- `gender`
- `region`
- `bmi`
- `cholesterol`
- `glucose`

### Synthetic Outliers Introduced

Extreme values are intentionally added to:

- `bmi`
- `blood_pressure`
- `cholesterol`
- `glucose`

### Target Variable

`disease_risk` is the target column:

- `0` → Low Risk
- `1` → High Risk

The target column is preserved during the cleaning workflow and is not imputed or modified.

---

## 🧪 Project Implementation

### 🔹 Part A — Handling Missing Values

First, the project checks the number and percentage of missing values in each column. It then demonstrates the following five approaches:

| No. | Technique | Implementation |
|---:|---|---|
| 1 | Simple Imputer | Median for numeric columns and most frequent for categorical columns |
| 2 | Most Frequent Imputation | Replaces missing categorical values with the most common category |
| 3 | Missing Indicator + Random Sample | Adds a missing-value flag and fills missing entries by sampling observed values |
| 4 | KNN Imputer | Estimates missing numeric values using nearby records |
| 5 | MICE / Iterative Imputer | Uses an iterative model to estimate missing numeric values |

**Note:** Standard `KNNImputer` and the project's MICE-style `IterativeImputer` are applied to numeric columns. Categorical columns are filled using most-frequent imputation.

### 🔹 Part B — Handling Outliers

The project identifies potential outliers in the four clinical measurement columns using:

1. **Z-Score Method:** Flags values whose absolute z-score is greater than 3.
2. **IQR Method:** Uses the lower and upper limits based on 1.5 × IQR.
3. **Percentile Method:** Checks values below the 1st percentile and above the 99th percentile.
4. **Winsorization:** Caps values at the 1st and 99th percentile limits instead of deleting entire records.

### 🔹 Part C — Final Clean Dataset

The final workflow:

- Uses the MICE-style imputed numeric values.
- Uses most-frequent imputation for categorical values.
- Applies Winsorization to the selected measurement columns.
- Checks for remaining missing values.
- Checks duplicate rows.
- Confirms that the row count is preserved.
- Confirms that `disease_risk` remains unchanged.
- Exports the cleaned dataset as a CSV file.

---

## 📊 Reports & Visualizations

The `Reports/` folder contains:

| File | Purpose |
|---|---|
| `Missing_Values_Report.csv` | Missing-value count and percentage by column |
| `Imputation_Method_Comparison.csv` | Comparison of imputation approaches |
| `Outlier_Detection_Report.csv` | Outlier counts using statistical methods |
| `Winsorization_Report.csv` | Lower and upper capping limits |
| `Before_After_Quality_Report.csv` | Dataset quality comparison |

The `Visualizations/` folder contains charts for:

- Missing values in the raw dataset.
- Outliers before treatment.
- Clinical measurements after Winsorization.
- Synthetic disease-risk class distribution.

---

## 📁 Project Folder Structure

```text
Patient_Health_Data_Preprocessing/
│
├── Dataset/
│   ├── raw_patient_data.csv
│   ├── mice_imputed_intermediate.csv
│   └── cleaned_patient_data.csv
│
├── Notebooks/
│   └── Patient_Health_Analysis.ipynb
│
├── Reports/
│   ├── Missing_Values_Report.csv
│   ├── Imputation_Method_Comparison.csv
│   ├── Outlier_Detection_Report.csv
│   ├── Winsorization_Report.csv
│   ├── Before_After_Quality_Report.csv
│   └── Concepts_and_Definitions.pdf
│
├── Scripts/
│   ├── generate_dataset.py
│   ├── missing_values.py
│   ├── outlier_treatment.py
│   └── final_validation.py
│
├── Visualizations/
│   ├── missing_values_before.png
│   ├── outliers_before.png
│   ├── outliers_after.png
│   └── disease_risk_distribution.png
│
├── Screenshots/
├── README.md
└── requirements.txt
```

---

## ⚙️ Technologies & Libraries

- **Python** — Main programming language.
- **Pandas** — Data loading, manipulation, and cleaning.
- **NumPy** — Numerical operations and synthetic data generation.
- **Matplotlib** — Data visualization.
- **Scikit-learn** — Imputation techniques.
- **Jupyter Notebook** — Interactive project implementation.

---

## 💻 Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Patient_Health_Data_Preprocessing
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Open Jupyter Notebook

```bash
jupyter notebook
```

### 5. Run the notebook

Open:

```text
Notebooks/Patient_Health_Analysis.ipynb
```

Run the notebook cells **from top to bottom**.

---

## ▶️ Running the Separate Python Scripts

The scripts are provided separately for practice. Run them from inside the `Scripts` directory so their relative file paths work.

```bash
cd Scripts
python generate_dataset.py
python missing_values.py
python outlier_treatment.py
python final_validation.py
```

**Execution order matters:** generate the raw dataset first, then run missing-value processing, outlier treatment, and final validation.

The Jupyter Notebook is also provided as a complete guided workflow.

---

## ✅ Final Validation Checklist

- [x] 5,000 synthetic records generated.
- [x] Missing values intentionally introduced.
- [x] Five missing-value approaches demonstrated.
- [x] Z-Score, IQR, and Percentile detection implemented.
- [x] Winsorization implemented.
- [x] Final cleaned CSV exported.
- [x] Target variable preserved in the generated final dataset.
- [x] Reports and visualizations created.
- [x] Concepts and definitions PDF included.

---

## 🧠 Learning Outcomes

After completing this project, students can:

- Understand common data-quality problems.
- Calculate missing-value counts and percentages.
- Compare different imputation techniques.
- Apply statistical methods to detect potential outliers.
- Understand how Winsorization limits extreme values.
- Validate and export a cleaned dataset.
- Document a data science project in a GitHub repository.

---

## ⚠️ Limitations & Responsible Use

- The dataset is synthetic and does not represent actual patients.
- `disease_risk` is an artificially generated educational label, not a medically validated diagnosis.
- Imputation results depend on the data and selected method.
- Statistical outlier flags do not automatically mean a value is incorrect.
- Real healthcare data requires privacy safeguards and review by qualified domain experts.

---

## 👨‍💻 Author

**Rami Ashutos**

*AI & Machine Learning Student*

---

<div align="center">

### ⭐ Thank You for Visiting This Project!

**If you find this project useful for learning, feel free to explore the code and reports.**

</div>
