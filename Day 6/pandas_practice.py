import os
import pandas as pd
import numpy as np

marks_series = pd.Series([85, 90, 78, 92], index=["Ali", "Sara", "Ahmed", "Fatima"])
print(marks_series)
print(marks_series.mean())

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Usman"],
    "Program": ["AI", "AI", "SE", "DS", "AI"],
    "Python": [85, 72, 90, 65, 78],
    "Math": [78, 75, 88, 70, 82]
}
df_sample = pd.DataFrame(data)
print(df_sample)

csv_path = "Day 6/student_performance.csv"
if not os.path.exists(csv_path):
    csv_path = "student_performance.csv"

df = pd.read_csv(csv_path)

print(df.head())
print(df.tail())
print(df.shape)
print(df.dtypes)
df.info()
print(df.describe())

print(df['Name'].head())
print(df[['Name', 'Program', 'Python']].head())
print(df.iloc[0:3])
print(df.iloc[2, 1])

print(df[df['Python'] >= 85][['Student_ID', 'Name', 'Program', 'Python']])
print(df[(df['Program'] == 'AI') & (df['Attendance'] >= 90)][['Name', 'Program', 'Attendance']])

sample_data = {
    "Student": ["Ali", "Sara", "Zain", "Hira"],
    "Python": [88, np.nan, 75, 92],
    "Math": [78, 85, np.nan, 90]
}
df_missing = pd.DataFrame(sample_data)
print(df_missing)
print(df_missing.isna())
print(df_missing.isna().sum())

df_filled = df_missing.copy()
df_filled['Python'] = df_filled['Python'].fillna(df_filled['Python'].mean())
df_filled['Math'] = df_filled['Math'].fillna(df_filled['Math'].mean())
print(df_filled)

print(df['Program'].value_counts())
numeric_cols = ['Python', 'Mathematics', 'Statistics', 'Machine_Learning', 'Attendance']
print(df.groupby('Program')[numeric_cols].mean())
