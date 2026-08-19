import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gradio as gr

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

def get_summary():
    total = len(df)
    subj_means = df[subjects].mean().round(2)
    highest_subj = f"{subj_means.idxmax()} ({subj_means.max()})"
    needs_imp = len(df[df['Performance'] == 'Needs Improvement'])
    return f"Total Students: {total}\nHighest Average Subject: {highest_subj}\nStudents Needing Improvement: {needs_imp}"

def filter_students(performance_filter, program_filter):
    filtered = df.copy()
    if performance_filter != "All":
        filtered = filtered[filtered['Performance'] == performance_filter]
    if program_filter != "All":
        filtered = filtered[filtered['Program'] == program_filter]
    return filtered[['Student_ID', 'Name', 'Program', 'Average_Score', 'Performance']]

def generate_chart(chart_type):
    fig, ax = plt.subplots(figsize=(8, 4))
    if chart_type == "Bar Chart (Average Score per Student)":
        sns.barplot(x='Name', y='Average_Score', data=df, ax=ax, hue='Name', legend=False)
        plt.xticks(rotation=45, ha='right')
        ax.set_title("Average Score per Student")
    elif chart_type == "Histogram (Score Distribution)":
        sns.histplot(df['Average_Score'], kde=True, bins=8, ax=ax)
        ax.set_title("Score Distribution")
    elif chart_type == "Scatter Plot (Python vs ML)":
        sns.scatterplot(x='Python', y='Machine_Learning', hue='Performance', data=df, ax=ax, s=90)
        ax.set_title("Python vs Machine Learning Marks")
    elif chart_type == "Pie Chart (Performance Breakdown)":
        counts = df['Performance'].value_counts()
        ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
        ax.set_title("Performance Categories Breakdown")
    elif chart_type == "Box Plot (Marks Across Subjects)":
        sns.boxplot(data=df[subjects], ax=ax)
        ax.set_title("Marks Across Core Subjects")
    plt.tight_layout()
    return fig

with gr.Blocks(title="Student Performance Dashboard") as app:
    gr.Markdown("# Student Performance Dashboard")
    
    with gr.Row():
        summary_box = gr.Textbox(label="Summary Metrics", value=get_summary(), interactive=False)
        
    with gr.Row():
        perf_dropdown = gr.Dropdown(choices=["All", "Excellent", "Good", "Average", "Needs Improvement"], value="All", label="Filter by Performance")
        prog_dropdown = gr.Dropdown(choices=["All", "AI", "DS", "SE"], value="All", label="Filter by Program")
        
    table_output = gr.Dataframe(value=df[['Student_ID', 'Name', 'Program', 'Average_Score', 'Performance']], label="Student Data")
    
    perf_dropdown.change(filter_students, inputs=[perf_dropdown, prog_dropdown], outputs=table_output)
    prog_dropdown.change(filter_students, inputs=[perf_dropdown, prog_dropdown], outputs=table_output)
    
    gr.Markdown("## Visualizations")
    chart_dropdown = gr.Dropdown(
        choices=[
            "Bar Chart (Average Score per Student)",
            "Histogram (Score Distribution)",
            "Scatter Plot (Python vs ML)",
            "Pie Chart (Performance Breakdown)",
            "Box Plot (Marks Across Subjects)"
        ],
        value="Bar Chart (Average Score per Student)",
        label="Select Chart"
    )
    plot_output = gr.Plot(value=generate_chart("Bar Chart (Average Score per Student)"))
    chart_dropdown.change(generate_chart, inputs=chart_dropdown, outputs=plot_output)

if __name__ == "__main__":
    app.launch(share=True)
