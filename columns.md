# Columns: Data Understanding

**Rows:** 5,000 | **Columns:** 16 | **Missing values:** none (all columns 5,000 non-null)

Roles: `ID` = identifier, `Feature` = input variable, `Target` = outcome variable.

---

## 1. Identity

| # | Column | Dtype | Non-Null | Values / Range | Role | Description |
|---|--------|-------|----------|----------------|------|-------------|
| 0 | `Student_ID` | str | 5000 | n/a | ID | Unique identifier for each student |
| 1 | `Age` | int64 | 5000 | 14 to 19 | Feature | Age of the student in years |
| 2 | `Gender` | str | 5000 | Male: 2447, Female: 2553 | Feature | Gender of the student |
| 3 | `Class` | int64 | 5000 | 9: 1218, 10: 1301, 11: 1262, 12: 1219 | Feature | Grade level the student is enrolled in |

## 2. Study Habits and Background

| # | Column | Dtype | Non-Null | Values / Range | Role | Description |
|---|--------|-------|----------|----------------|------|-------------|
| 4 | `Study_Hours_Per_Day` | float64 | 5000 | continuous | Feature | Average hours the student studies per day |
| 5 | `Attendance_Percentage` | int64 | 5000 | continuous (percent) | Feature | Percentage of classes attended |
| 6 | `Parental_Education` | str | 5000 | Postgraduate: 1679, Graduate: 1661, High School: 1660 | Feature | Highest education level of the student's parents |
| 7 | `Internet_Access` | str | 5000 | No: 2622, Yes: 2378 | Feature | Whether the student has internet access at home |
| 8 | `Extracurricular_Activities` | str | 5000 | Yes: 2519, No: 2481 | Feature | Whether the student takes part in extracurricular activities |

## 3. Scores

| # | Column | Dtype | Non-Null | Values / Range | Role | Description |
|---|--------|-------|----------|----------------|------|-------------|
| 9 | `Math_Score` | int64 | 5000 | numeric score | Feature | Student's score in Math |
| 10 | `Science_Score` | int64 | 5000 | numeric score | Feature | Student's score in Science |
| 11 | `English_Score` | int64 | 5000 | numeric score | Feature | Student's score in English |
| 12 | `Previous_Year_Score` | int64 | 5000 | numeric score | Feature | Student's overall score in the previous academic year |

## 4. Targets

| # | Column | Dtype | Non-Null | Values / Range | Role | Description |
|---|--------|-------|----------|----------------|------|-------------|
| 13 | `Final_Percentage` | float64 | 5000 | continuous (percent) | Target | Student's final overall percentage |
| 14 | `Performance_Level` | str | 5000 | Good: 2191, Average: 1951, Excellent: 593, Poor: 265 | Target | Categorical performance rating |
| 15 | `Pass_Fail` | str | 5000 | Pass: 4735, Fail: 265 | Target | Whether the student passed or failed |

---

## Summary by Dtype

| Dtype | Count | Columns |
|-------|-------|---------|
| str | 7 | `Student_ID`, `Gender`, `Parental_Education`, `Internet_Access`, `Extracurricular_Activities`, `Performance_Level`, `Pass_Fail` |
| int64 | 7 | `Age`, `Class`, `Attendance_Percentage`, `Math_Score`, `Science_Score`, `English_Score`, `Previous_Year_Score` |
| float64 | 2 | `Study_Hours_Per_Day`, `Final_Percentage` |