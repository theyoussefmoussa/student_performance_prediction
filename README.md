<p align="center">
  <img src="assets/banner.jpeg" alt="Student Performance Prediction banner" width="100%">
</p>

# Student Performance Prediction

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=matplotlib&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)

A data science project that analyzes student records and builds models to predict academic performance.

---

## Project Goal

The goal of this project is to **predict whether a student will pass or fail** based on the features in the dataset, such as demographics, study habits, attendance, parental education, and subject scores.

This is a **binary classification** problem, and the target column is `Pass_Fail` (encoded as `Pass` = 1 and `Fail` = 0 in the cleaned data).

---

## Dataset Overview

The raw dataset (`data/raw/student_performance_data.csv`) contains **5,000 students** and **16 columns**, with no missing values.

| Group | Columns |
|-------|---------|
| Identity | `Student_ID`, `Age`, `Gender`, `Class` |
| Study habits and background | `Study_Hours_Per_Day`, `Attendance_Percentage`, `Parental_Education`, `Internet_Access`, `Extracurricular_Activities` |
| Scores | `Math_Score`, `Science_Score`, `English_Score`, `Previous_Year_Score` |
| Targets | `Final_Percentage`, `Performance_Level`, `Pass_Fail` |

The cleaned version (5,000 rows, 11 columns) is saved as `data/processed/student_performance_cleaned.parquet` and is the input for the EDA and modeling phases. See [`data_cleaning.md`](data_cleaning.md) for how it was produced.

See [`columns.md`](columns.md) for the full data dictionary: dtypes, categories, value counts, roles, and descriptions.

---

## Project Phases

`Data Understanding` → `Data Cleaning & Preprocessing` → `EDA` → `Modeling`

| # | Phase | Status | Deliverable |
|---|-------|--------|-------------|
| 1 | Data Understanding | ✅ Done | `notebooks/1_data_understanding.ipynb`, `columns.md` |
| 2 | Data Cleaning & Preprocessing | ✅ Done | `notebooks/2_data_cleaning.ipynb`, `src/data_cleaning.py`, `data_cleaning.md`, `data/processed/student_performance_cleaned.parquet` |
| 3 | EDA | ⏳ Pending | EDA notebook |
| 4 | Modeling | ⏳ Pending | Trained models and evaluation |

---

## Project Structure

```
student_performance_prediction/
├── assets/
│   └── banner.jpeg
├── data/
│   ├── raw/
│   │   └── student_performance_data.csv
│   └── processed/
│       └── student_performance_cleaned.parquet
├── notebooks/
│   ├── 1_data_understanding.ipynb
│   └── 2_data_cleaning.ipynb
├── src/
│   └── data_cleaning.py
├── .gitignore
├── columns.md
├── data_cleaning.md
├── main.py
└── setup.md
```

---

## Getting Started

To run the project on your machine, follow the step-by-step guide in [`setup.md`](setup.md). It covers **Linux** and **Windows (CMD)**.

---

## Credits

Built by **Youssef Moussa**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/theyoussefmoussa) [![Portfolio](https://img.shields.io/badge/Portfolio-Visit-000000?style=for-the-badge&logo=githubpages&logoColor=white)](https://theyoussefmoussa.github.io)