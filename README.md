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

## Project Phases

`Data Understanding` → `Data Cleaning & Preprocessing` → `EDA` → `Modeling`

| # | Phase | Status | Deliverable |
|---|-------|--------|-------------|
| 1 | Data Understanding | ✅ Done | `notebooks/1_data_understanding.ipynb`, `columns.md` |
| 2 | Data Cleaning & Preprocessing | ⏳ Pending | Cleaned dataset |
| 3 | EDA | ⏳ Pending | EDA notebook |
| 4 | Modeling | ⏳ Pending | Trained models and evaluation |

---

## Dataset Overview

The dataset (`data/raw/student_performance_data.csv`) contains **5,000 students** and **16 columns**, with no missing values. The columns cover student demographics, study habits, subject scores, and performance outcomes.

See [`columns.md`](columns.md) for the full data dictionary: dtypes, categories, value counts, roles, and descriptions.

---

## Project Structure

```
student_performance_prediction/
├── assets/
│   └── banner.jpeg
├── data/
│   └── raw/
│       └── student_performance_data.csv
├── notebooks/
│   └── 1_data_understanding.ipynb
├── .gitignore
├── columns.md
├── main.py
└── requirements.txt
```

---

## Getting Started

### 1. Clone the project

```bash
git clone https://github.com/theyoussefmoussa/student_performance_prediction.git
cd student_performance_prediction
```

### 2. Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate
```

On Windows, activate with `.venv\Scripts\activate` instead.

### 3. Install the requirements

```bash
uv pip install -r requirements.txt
```

---

## Usage

Run the main script from the project root:

```bash
python3 main.py
```
On Windows, run `python main.py` instead. <br>
To explore the data understanding phase, open the notebook:

```bash
jupyter notebook notebooks/1_data_understanding.ipynb
```

---

## Credits

Built by **Youssef Moussa**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/theyoussefmoussa) [![Portfolio](https://img.shields.io/badge/Portfolio-Visit-000000?style=for-the-badge&logo=githubpages&logoColor=white)](https://theyoussefmoussa.github.io)