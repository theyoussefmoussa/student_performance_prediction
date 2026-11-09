import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv
from utils.visualize_helper import (highlight_max, title_labels, annotate_bars, save_plot)


def univariate_analysis():
    load_dotenv()
    project_root= os.getenv('PROJECT_ROOT')
    df = pd.read_parquet(f"{project_root}/data/processed/student_performance_cleaned.parquet")

    # distribution of Study Hours
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(
        df['Study_Hours_Per_Day'],
        bins=20,
        color='skyblue',
        edgecolor='black'
    )
    title_labels(
        'Distribution of Study Hours Per Day',
        'Study Hours Per Day',
        'Frequency'
    )
    annotate_bars(ax)
    highlight_max(ax)
    save_plot(fig, 'study_hours_distribution.png')

    # distribution of Students by Class 
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.countplot(
        x='Class',
        data=df,
        ax=ax
    )
    highlight_max(ax)
    title_labels(
        'Distribution of Students by Class',
        'Class',
        'Number of Students'
    )
    annotate_bars(ax)
    save_plot(fig, 'students_by_class_distribution.png')

    # distribution of Students by Age
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.countplot(
        x = 'Age',
        data=df,
        ax=ax
    )
    title_labels(
        'Distribution of Students by Age',
        'Age',
        'Number of Students'
    )
    highlight_max(ax)
    annotate_bars(ax)
    save_plot(fig, 'students_by_age_distribution.png')

    # distribution of Students by Attendance Percentage
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(
        df['Attendance_Percentage'],
        bins=20,
        edgecolor='black'
    )
    title_labels(
        'Distribution of Students by Attendance Percentage',
        'Attendance Percentage',
        'Number of Students'
    )
    plt.xticks(np.arange(50, 105, 5))
    highlight_max(ax)
    annotate_bars(ax)
    save_plot(fig, 'students_by_attendance_distribution.png')

    # distribution of Students by Internet Access
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.pie(
        df['Internet_Access'].value_counts(),
        labels=df['Internet_Access'].value_counts().index,
        autopct= '%1.1f%%',
    )
    plt.legend(title='Internet Access', loc='upper right')
    save_plot(fig, 'students_by_internet_access_distribution.png')

    # distribution of Students by Extracurricular Activities
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.pie(
        df['Extracurricular_Activities'].value_counts(),
        labels=df['Extracurricular_Activities'].value_counts().index,
        autopct= '%1.1f%%',
    )
    plt.legend(title='Extracurricular Activities', loc='upper right')
    save_plot(fig, 'students_by_extracurricular_activities_distribution.png')

    # distribution of Previous Year Score
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(
        df['Previous_Year_Score'],
        bins=20,
        edgecolor='black')

    highlight_max(ax)
    annotate_bars(ax)
    title_labels(
        'Distribution of Students by Previous Year Score',
        'Previous Year Score',
        'Number of Students'
    )
    save_plot(fig, 'students_by_previous_year_score_distribution.png')

    # distribution of Students by Gender
    fig, ax = plt.subplots(figsize=(10, 8))
    gender_map= {1: 'Male', 0: 'Female'}
    plt.pie(
        df['Is_Male'].value_counts(),
        labels=[gender_map[i] for i in df['Is_Male'].value_counts().index],
        autopct= '%1.1f%%'
    )
    plt.legend(title='Gender', loc='upper right')
    save_plot(fig, 'students_by_gender_distribution.png')

    # Distribution of Parent Education
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(
        x = 'Parental_Education',
        data=df,
        ax=ax
    )
    annotate_bars(ax)
    highlight_max(ax)
    title_labels(
        'Distribution of Students by Parental Education',
        'Parental Education',
        'Number of Students'
    )
    save_plot(fig, 'students_by_parental_education_distribution.png')

    print("All Graphs Saved to ouputs/univariate_analysis/")
    print("Univariate Analysis Complete")