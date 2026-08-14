import os
import pandas as pd
import numpy as np

def assign_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'F'

csv_path = "Day 6/student_performance.csv"
if not os.path.exists(csv_path):
    csv_path = "student_performance.csv"

out_path = "Day 6/analyzed_student_performance.csv"
if not os.path.exists("Day 6"):
    out_path = "analyzed_student_performance.csv"

df = pd.read_csv(csv_path)

print(len(df))
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())

subjects = ['Python', 'Mathematics', 'Statistics', 'Machine_Learning']
for s in subjects:
    print(s, df[s].mean(), df[s].max(), df[s].min())

df['Total_Marks'] = df[subjects].sum(axis=1)
df['Percentage'] = (df['Total_Marks'] / 400) * 100
df['Grade'] = df['Percentage'].apply(assign_grade)

class_avg = df['Percentage'].mean()
df['Performance_Status'] = np.where(df['Percentage'] >= class_avg, 'Above Average', 'Below Average')

top_5 = df.sort_values(by='Total_Marks', ascending=False).head(5)
print(top_5[['Student_ID', 'Name', 'Program', 'Total_Marks', 'Percentage', 'Grade', 'Attendance']])

below_avg = df[df['Percentage'] < class_avg]
print(below_avg[['Student_ID', 'Name', 'Program', 'Total_Marks', 'Percentage', 'Grade', 'Performance_Status']])

numeric_cols = ['Python', 'Mathematics', 'Statistics', 'Machine_Learning', 'Percentage', 'Attendance']
print(df.groupby('Program')[numeric_cols].mean())

df.to_csv(out_path, index=False)
