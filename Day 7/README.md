# Day 7: Data Cleaning & Visualization

Welcome to Day 7 of the MLB Internship curriculum. Today's focus is on Data Cleaning using Pandas, Data Visualization using Matplotlib and Seaborn, building an interactive Student Performance Dashboard using Gradio and Streamlit, and running the workflow on Google Colab with Ngrok integration.

---

## Overview & Topics Covered

### 1. Data Cleaning (Pandas)
- Checking and handling missing values (`df.isna().sum()`).
- Removing duplicate records (`df.drop_duplicates()`).
- Standardizing column names and converting data types (`pd.to_numeric`).
- Creating calculated columns (`Average_Score`).
- Creating categorical performance metrics (`Performance`):
  - Excellent: >= 90
  - Good: 80-89
  - Average: 70-79
  - Needs Improvement: < 70
- Sorting and filtering dataset records.
- Exporting the cleaned dataset to `cleaned_student_performance.csv`.

### 2. Data Visualization (Matplotlib & Seaborn)
- Bar Chart: Average score per student.
- Histogram: Distribution of average scores across the class.
- Scatter Plot: Python marks vs Machine Learning marks grouped by performance and program.
- Pie Chart: Proportion of students across performance categories.
- Box Plot: Distribution of marks across Python, Mathematics, Statistics, and Machine Learning subjects.
- Automatic exporting of plots to PNG image files.

### 3. Student Performance Dashboard (Gradio & Streamlit + Ngrok)
- Interactive web apps displaying key metrics: total students, subject with highest average, and students needing improvement count.
- Interactive filtering by Performance Tier and Academic Program.
- Embedded live Matplotlib/Seaborn visualization plots.
- Public sharing links and Ngrok integration for URL deployment.

---

## Repository & Folder Structure

```
Day 7/
│
├── student_performance.csv                 # Raw Input Dataset (20 Student Records)
├── cleaned_student_performance.csv         # Cleaned & Transformed Dataset
├── data_cleaning.py                        # Data Cleaning Script
├── data_visualization.py                   # Data Visualization Script (Generates PNGs)
├── gradio_app.py                           # Gradio Dashboard Web App
├── dashboard_app.py                        # Streamlit Dashboard App
├── Day7_Data_Cleaning_and_Visualization.ipynb  # Google Colab Notebook with Gradio & Ngrok
├── bar_chart.png                           # Exported Bar Chart
├── histogram.png                           # Exported Histogram
├── scatter_plot.png                        # Exported Scatter Plot
├── pie_chart.png                           # Exported Pie Chart
├── box_plot.png                            # Exported Box Plot
└── README.md                               # Technical Documentation
```

---

## Data Cleaning Steps

1. **Ingestion & Inspection**: Loaded `student_performance.csv` and confirmed 0 missing values across all columns.
2. **Deduplication**: Verified uniqueness across student records (`Student_ID`).
3. **Column Normalization**: Stripped whitespace and replaced space separators with underscores.
4. **Data Type Conversion**: Converted subject score columns (`Python`, `Mathematics`, `Statistics`, `Machine_Learning`) into numeric types.
5. **Feature Engineering**:
   - `Average_Score`: Calculated average mark across the 4 core subjects for each student.
   - `Performance`: Mapped `Average_Score` into performance tiers (`Excellent`, `Good`, `Average`, `Needs Improvement`).
6. **Export**: Saved transformed dataset as `cleaned_student_performance.csv`.

---

## Visualizations Created

1. `bar_chart.png`: Visualizes average score per student sorted by performance rank.
2. `histogram.png`: Displays frequency distribution of overall average marks.
3. `scatter_plot.png`: Evaluates correlation between Python and Machine Learning scores.
4. `pie_chart.png`: Illustrates the percentage split of performance categories (`Excellent`, `Good`, `Average`, `Needs Improvement`).
5. `box_plot.png`: Compares spread, median, quartiles, and outliers across all four subjects.

---

## Key Insights

1. **Top Performance**: Laiba Khan (Software Engineering) achieved the highest overall average score of **97.25%**, followed by Ayesha Malik (95.50%) and Noor Fatima (92.50%).
2. **Subject Strengths**: Machine Learning recorded the highest subject-wide average score (**82.60**), while Python recorded the lowest average score (**78.90**).
3. **At-Risk Identification**: 4 students fell into the "Needs Improvement" category (`Average_Score` < 70%): Hassan Tariq (DS, 58.75%), Danish Ali (SE, 64.00%), Fatima Noor (DS, 68.75%), and Abdullah (DS, 69.00%).

---

## How to Run locally

### 1. Run Data Cleaning Script
```bash
python "Day 7/data_cleaning.py"
```

### 2. Run Data Visualization Script
```bash
python "Day 7/data_visualization.py"
```

### 3. Launch Gradio Dashboard App
```bash
python "Day 7/gradio_app.py"
```

### 4. Launch Streamlit Dashboard App
```bash
streamlit run "Day 7/dashboard_app.py"
```

---

## How to Run on Google Colab with Gradio & Ngrok

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload `Day7_Data_Cleaning_and_Visualization.ipynb` (found in the `Day 7` directory of this repo).
3. Execute the notebook cells sequentially:
   - Cell 1 installs `pandas`, `matplotlib`, `seaborn`, `gradio`, and `pyngrok`.
   - Cell 2 runs the data cleaning logic and saves `cleaned_student_performance.csv`.
   - Cell 3 generates and displays all 5 visualizations inline.
   - Cell 4 launches the Gradio dashboard directly with a public share link (`share=True`).
   - Cell 5 (Optional) opens a public Ngrok tunnel to local port 7860.
4. Copy the generated public URL for task evaluation.
