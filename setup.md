# Setup Guide

This guide walks you through setting up and running the project on **Linux** and **Windows (CMD)**. Follow the steps in order and use the check after each one to confirm it worked.

[← Back to README](README.md)

---

## 1. Clone the project

Same on Linux and Windows:

```bash
git clone https://github.com/theyoussefmoussa/student_performance_prediction.git
cd student_performance_prediction
```

---

## 2. Install uv

[uv](https://docs.astral.sh/uv/) is the Python package and environment manager used in this project. First check whether it is already installed.

### Linux

```bash
uv --version
```

If you see a version number (for example `uv 0.x.x`), skip to step 3. If you get `command not found`, install it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Reload your shell so the `uv` command is available:

```bash
source $HOME/.local/bin/env
```

### Windows (CMD)

```cmd
uv --version
```

If you see a version number, skip to step 3. If you get `'uv' is not recognized as an internal or external command`, install it:

```cmd
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then **close the CMD window and open a new one** so the `uv` command is available. Go back to the project folder:

```cmd
cd student_performance_prediction
```

### Check

```bash
uv --version
```

You should see a version number such as `uv 0.x.x`.

---

## 3. Create and activate a virtual environment

### Linux

```bash
uv venv
source .venv/bin/activate
```

### Windows (CMD)

```cmd
uv venv
.venv\Scripts\activate
```

### Check

Your terminal prompt should now start with `(student_performance_prediction)` or `(.venv)`.

---

## 4. Install the dependencies

Same on Linux and Windows:

```bash
uv pip install pandas numpy matplotlib scikit-learn pyarrow python-dotenv jupyter
```

| Package | Used for |
|---------|----------|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` | Visualizations |
| `scikit-learn` | Modeling |
| `pyarrow` | Reading and writing the parquet file |
| `python-dotenv` | Loading `PROJECT_ROOT` from the `.env` file |
| `jupyter` | Running the notebooks |

### Check

```bash
uv pip list
```

All the packages above should appear in the list.

---

## 5. Configure the project

The cleaning script reads the project location from a `.env` file and writes its output to `data/processed/`. Run these commands from the project root.

### Linux

Create the `.env` file with the current folder as `PROJECT_ROOT`, and make sure the output folder exists:

```bash
echo "PROJECT_ROOT=$(pwd)" > .env
mkdir -p data/processed
```

### Windows (CMD)

Do not put a space before `>` in the first command, or the path will end with a trailing space. If `mkdir` says the folder already exists, you can ignore it.

```cmd
echo PROJECT_ROOT=%cd%> .env
mkdir data\processed
```

### Check

Linux:

```bash
cat .env
```

Windows (CMD):

```cmd
type .env
```

You should see one line with the full path to the project folder, for example `PROJECT_ROOT=/home/you/student_performance_prediction`.

---

## 6. Run the project

Run the main script from the project root. It runs `src/data_cleaning.py` and writes the cleaned dataset to `data/processed/student_performance_cleaned.parquet`. See [`data_cleaning.md`](data_cleaning.md) for what the cleaning does.

### Linux

```bash
python3 main.py
```

### Windows (CMD)

```cmd
python main.py
```

### Check

The script should print the shape after cleaning (`(5000, 11)`) and `Cleaned data saved to parquet file.`, and the file `data/processed/student_performance_cleaned.parquet` should now exist.

---

## 7. Explore the notebooks

Same on Linux and Windows:

```bash
jupyter notebook notebooks/1_data_understanding.ipynb
jupyter notebook notebooks/2_data_cleaning.ipynb
```

| Notebook | Phase |
|----------|-------|
| `1_data_understanding.ipynb` | Data Understanding |
| `2_data_cleaning.ipynb` | Data Cleaning & Preprocessing |