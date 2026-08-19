import os
import pandas as pd

def assign_performance(score):
    if score >= 90:
        return 'Excellent'
    elif score >= 80:
        return 'Good'
    elif score >= 70:
        return 'Average'
    else:
        return 'Needs Improvement'

csv_path = "Day 7/student_performance.csv"
if not os.path.exists(csv_path):
    csv_path = "student_performance.csv"

out_path = "Day 7/cleaned_student_performance.csv"
if not os.path.exists("Day 7"):
    out_path = "cleaned_student_performance.csv"

df = pd.read_csv(csv_path)

print(df.isna().sum())

df = df.drop_duplicates()

df.columns = [col.strip().replace(" ", "_") for col in df.columns]

subjects = ['Python', 'Mathematics', 'Statistics', 'Machine_Learning']
for col in subjects:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['Average_Score'] = df[subjects].mean(axis=1).round(2)
df['Performance'] = df['Average_Score'].apply(assign_performance)

df = df.sort_values(by='Average_Score', ascending=False)

print(df.head())
print(df['Performance'].value_counts())

df.to_csv(out_path, index=False)
