import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_path = "Day 7/cleaned_student_performance.csv"
if not os.path.exists(csv_path):
    csv_path = "cleaned_student_performance.csv"

if not os.path.exists(csv_path):
    import data_cleaning

df = pd.read_csv(csv_path)

out_dir = "Day 7"
if not os.path.exists(out_dir):
    out_dir = "."

plt.figure(figsize=(10, 5))
sns.barplot(x='Name', y='Average_Score', data=df, hue='Name', legend=False)
plt.xticks(rotation=45, ha='right')
plt.title('Average Score per Student')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'bar_chart.png'))
plt.close()

plt.figure(figsize=(8, 5))
sns.histplot(df['Average_Score'], kde=True, bins=8)
plt.title('Average Score Distribution')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'histogram.png'))
plt.close()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='Python', y='Machine_Learning', hue='Performance', style='Program', s=100, data=df)
plt.title('Python vs Machine Learning Marks')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'scatter_plot.png'))
plt.close()

plt.figure(figsize=(6, 6))
counts = df['Performance'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Performance Categories Distribution')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'pie_chart.png'))
plt.close()

plt.figure(figsize=(8, 5))
subjects = ['Python', 'Mathematics', 'Statistics', 'Machine_Learning']
sns.boxplot(data=df[subjects])
plt.title('Marks Distribution Across All Subjects')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'box_plot.png'))
plt.close()

print("Saved all 5 PNG visualizations.")
