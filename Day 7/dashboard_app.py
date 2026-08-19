import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

csv_path = "Day 7/cleaned_student_performance.csv"
if not os.path.exists(csv_path):
    csv_path = "cleaned_student_performance.csv"

if not os.path.exists(csv_path):
    raw_path = "Day 7/student_performance.csv"
    if not os.path.exists(raw_path):
        raw_path = "student_performance.csv"
    df = pd.read_csv(raw_path)
    subjects = ['Python', 'Mathematics', 'Statistics', 'Machine_Learning']
    df['Average_Score'] = df[subjects].mean(axis=1).round(2)
    def assign_perf(s):
        if s >= 90: return 'Excellent'
        elif s >= 80: return 'Good'
        elif s >= 70: return 'Average'
        else: return 'Needs Improvement'
    df['Performance'] = df['Average_Score'].apply(assign_perf)
else:
    df = pd.read_csv(csv_path)

subjects = ['Python', 'Mathematics', 'Statistics', 'Machine_Learning']

st.title("Student Performance Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Total Students", len(df))
subject_means = df[subjects].mean().round(2)
highest_subject = subject_means.idxmax()
col2.metric("Subject with Highest Avg", f"{highest_subject} ({subject_means[highest_subject]})")
needs_imp_count = len(df[df['Performance'] == 'Needs Improvement'])
col3.metric("Students Needing Improvement", needs_imp_count)

st.subheader("Average Score per Subject")
st.dataframe(subject_means.to_frame(name="Average Marks"))

col_top, col_imp = st.columns(2)

with col_top:
    st.subheader("Top 5 Performing Students")
    st.dataframe(df.sort_values(by='Average_Score', ascending=False).head(5)[['Student_ID', 'Name', 'Program', 'Average_Score', 'Performance']])

with col_imp:
    st.subheader("Students Needing Improvement")
    st.dataframe(df[df['Performance'] == 'Needs Improvement'][['Student_ID', 'Name', 'Program', 'Average_Score', 'Performance']])

st.subheader("Visualizations")
c1, c2 = st.columns(2)

with c1:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x='Name', y='Average_Score', data=df, ax=ax, hue='Name', legend=False)
    plt.xticks(rotation=45, ha='right')
    ax.set_title("Average Score per Student")
    st.pyplot(fig)

with c2:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(x='Python', y='Machine_Learning', hue='Performance', data=df, ax=ax, s=90)
    ax.set_title("Python vs Machine Learning Marks")
    st.pyplot(fig)

c3, c4 = st.columns(2)

with c3:
    fig, ax = plt.subplots(figsize=(6, 4))
    counts = df['Performance'].value_counts()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title("Performance Distribution")
    st.pyplot(fig)

with c4:
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.boxplot(data=df[subjects], ax=ax)
    ax.set_title("Marks Across Subjects")
    st.pyplot(fig)
