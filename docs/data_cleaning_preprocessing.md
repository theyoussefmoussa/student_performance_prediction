# Data Cleaning & Preprocessing

This document describes what was done in the **Data Cleaning & Preprocessing** phase.

| | |
|---|---|
| **Input** | `data/raw/student_performance_data.csv` (5,000 rows, 16 columns) |
| **Output** | `data/processed/student_performance_cleaned.parquet` (5,000 rows, 11 columns) |
| **Script** | `src/data_cleaning.py` (function `data_cleaning()`) |
| **Notebook** | `notebooks/2_data_cleaning.ipynb` |

[← Back to README](README.md)

---

## What I Did

1. Converted and encoded columns to better datatypes
2. Dropped the identifier column and the columns that cause data leakage
3. Saved the cleaned dataset as a parquet file

---

## 1. Convert and Encode Columns

Smaller and more specific datatypes reduce memory usage and make the meaning of each column clearer. Binary columns are encoded as 0/1 so they are ready for modeling.

| Column | Before | After | Reason |
|--------|--------|-------|--------|
| `Age` | int64 | uint8 | Values range from 14 to 19, which fits in 0 to 255 |
| `Attendance_Percentage` | int64 | uint8 | Percentage values fit in 0 to 255 |
| `Pass_Fail` | str | uint8 | Target encoded as `Fail` = 0, `Pass` = 1 |
| `Gender` | str | `Is_Male` (uint8) | Binary column: `Male` = 1, `Female` = 0. `Gender` is dropped after the new column is created |
| `Internet_Access` | str | bool | Binary column: `Yes` = True, `No` = False |
| `Extracurricular_Activities` | str | bool | Binary column: `Yes` = True, `No` = False |
| `Class` | int64 | category | Grade levels (9 to 12) are treated as plain classes, not quantities |
| `Parental_Education` | str | one-hot columns | Encoded with `drop_first=True` into `Parent_Education_High School` and `Parent_Education_Postgraduate`. `Graduate` is the baseline (all zeros), which avoids redundant columns |

Columns left unchanged: `Study_Hours_Per_Day` (float64) and `Previous_Year_Score` (int64).

---

## 2. Drop Columns

| Column | Reason |
|--------|--------|
| `Student_ID` | Identifier with no predictive value |
| `Gender` | Replaced by `Is_Male` |
| `Final_Percentage` | `Pass_Fail` is a threshold on it (Fail maximum 49.67, Pass minimum 50.00), so it reveals the target directly. Dropped to prevent data leakage |
| `Performance_Level` | Derived from the outcome. Dropped to prevent data leakage |
| `Math_Score` | `Final_Percentage` is the mean of the three subject scores (maximum difference 0.0033, which is rounding), so together they determine the target. Dropped to prevent data leakage |
| `Science_Score` | Same reason as `Math_Score` |
| `English_Score` | Same reason as `Math_Score` |

---

## 3. Save the Cleaned Dataset

The cleaned dataset is saved to `data/processed/student_performance_cleaned.parquet`.

Parquet is used instead of CSV because it keeps the datatypes from step 1 (`uint8` and `bool`). A CSV file would lose them and they would need to be converted again on every load.

**Note:** `Class` is a category with integer values (9 to 12), and it can come back as `int64` when the parquet file is read (seen with pandas 3.0.2 and pyarrow 26.0.0). After loading, convert it again:

```python
df = pd.read_parquet("data/processed/student_performance_cleaned.parquet")
df['Class'] = df['Class'].astype('category')
```

---

## Final Schema

The cleaned dataset has **5,000 rows** and **11 columns**:

| # | Column | Dtype | Role |
|---|--------|-------|------|
| 1 | `Age` | uint8 | Feature |
| 2 | `Class` | category | Feature |
| 3 | `Study_Hours_Per_Day` | float64 | Feature |
| 4 | `Attendance_Percentage` | uint8 | Feature |
| 5 | `Internet_Access` | bool | Feature |
| 6 | `Extracurricular_Activities` | bool | Feature |
| 7 | `Previous_Year_Score` | int64 | Feature |
| 8 | `Pass_Fail` | uint8 | Target |
| 9 | `Is_Male` | uint8 | Feature |
| 10 | `Parent_Education_High School` | bool | Feature |
| 11 | `Parent_Education_Postgraduate` | bool | Feature |

---

## How to Run

Follow [`setup.md`](setup.md), then run from the project root:

```bash
python3 main.py
```