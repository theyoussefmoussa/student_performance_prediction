# Univariate Analysis

This document describes what was done in the **Univariate Analysis** phase.

| | |
|---|---|
| **Input** | `data/processed/student_performance_cleaned.parquet` (5,000 rows, 10 columns) |
| **Output** | 9 plots (PNG) in `outputs/univariate_analysis/` |
| **Script** | `src/univariate_analysis.py` (function `univariate_analysis()`) |
| **Notebook** | `notebooks/3_univariate_analysis.ipynb` |

[← Back to README](../README.md)

---

## What I Did

1. Loaded the cleaned dataset
2. Plotted the distribution of each feature on its own, using the chart type that fits the column
3. Saved every plot as a PNG file

---

## 1. Choose the Chart Type

Each column is plotted according to its type:

| Column type | Chart | Why |
|-------------|-------|-----|
| Continuous or wide-range numeric | Histogram (20 bins) | Shows the shape of the distribution |
| Discrete with few values | Count plot | One bar per value, so every value is visible |
| Binary | Pie chart with percentages | Only two parts, so the split is easy to read |
| Categorical | Count plot | Compares the size of each category |

---

## 2. Plots

| # | Column | Chart | Output file |
|---|--------|-------|-------------|
| 1 | `Study_Hours_Per_Day` | Histogram, 20 bins | `study_hours_distribution.png` |
| 2 | `Class` | Count plot | `students_by_class_distribution.png` |
| 3 | `Age` | Count plot | `students_by_age_distribution.png` |
| 4 | `Attendance_Percentage` | Histogram, 20 bins, x-axis ticks every 5 from 50 to 100 | `students_by_attendance_distribution.png` |
| 5 | `Internet_Access` | Pie chart | `students_by_internet_access_distribution.png` |
| 6 | `Extracurricular_Activities` | Pie chart | `students_by_extracurricular_activities_distribution.png` |
| 7 | `Previous_Year_Score` | Histogram, 20 bins | `students_by_previous_year_score_distribution.png` |
| 8 | `Is_Male` | Pie chart, labeled `Male` and `Female` | `students_by_gender_distribution.png` |
| 9 | `Parental_Education` | Count plot | `students_by_parental_education_distribution.png` |

Columns not covered here: `Pass_Fail` (the target).

---

## 3. Plot Helpers

The formatting is shared through helper functions in `utils/visualize_helper.py`, so all plots look the same:

| Helper | Purpose |
|--------|---------|
| `title_labels` | Sets the title and the axis labels |
| `annotate_bars` | Writes the value on top of each bar |
| `highlight_max` | Highlights the tallest bar |
| `save_plot` | Saves the figure as a PNG file |

The histograms and count plots use all of these helpers. The pie charts only show percentages and a legend, and are saved with `save_plot`.

---

## 4. Save the Plots

Each figure is saved as a PNG file in `outputs/univariate_analysis/`. When the function finishes, it prints `Univariate Analysis Complete`.

---

## How to Run

Follow [`setup.md`](setup.md) and run the cleaning phase first, because this phase reads the cleaned parquet file. Then run from the project root:

```bash
python3 main.py
```