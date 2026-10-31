import os

import pandas as pd
from dotenv import load_dotenv
from sklearn.preprocessing import LabelEncoder


def data_cleaning():
    # load data
    load_dotenv()
    PROJECT_ROOT = os.getenv('PROJECT_ROOT')
    df = pd.read_csv(f"{PROJECT_ROOT}/data/raw/student_performance_data.csv")

    # encode Gender as Is_Male (1 = Male, 0 = Female)
    df['Is_Male'] = (df['Gender'] == 'Male').astype('uint8')

    # binary columns -> bool
    df['Internet_Access'] = df['Internet_Access'].map({"Yes": 1, "No": 0})
    df['Extracurricular_Activities'] = df['Extracurricular_Activities'].map({"Yes": 1, "No": 0})

    binary_cols = ['Internet_Access', 'Extracurricular_Activities']
    for col in binary_cols:
        df[col] = df[col].astype('bool')

    # Class -> category, Parental_Education -> one-hot (first category dropped)
    df['Class'] = df['Class'].astype('category')
    df = pd.get_dummies(df, columns=['Parental_Education'], prefix='Parent_Education', drop_first=True)

    # encode target: Fail = 0, Pass = 1
    le = LabelEncoder()
    df['Pass_Fail'] = le.fit_transform(df['Pass_Fail'])

    # change to uint8
    uint8_cols = ['Age', 'Attendance_Percentage', 'Pass_Fail']
    for col in uint8_cols:
        df[col] = df[col].astype('uint8')

    # columns to be dropped
    cols_to_drop = ['Student_ID', 'Performance_Level', 'Final_Percentage',
                    'Math_Score', 'English_Score', 'Science_Score', 'Gender']
    df = df.drop(columns=cols_to_drop)

    print(f"Data shape after cleaning: {df.shape}")

    # save new dataset
    df.to_parquet(f"{PROJECT_ROOT}/data/processed/student_performance_cleaned.parquet")
    print("Cleaned data saved to parquet file.")
    return df