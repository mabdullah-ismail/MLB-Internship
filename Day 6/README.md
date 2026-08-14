# Day 6: Python for Data Science (NumPy & Pandas)

Welcome to **Day 6** of the MLB Internship curriculum! Today's focus transitions into **Data Handling and Analysis** using two foundational Python libraries in AI & Data Science: **NumPy** and **Pandas**.

---

## Overview & Topics Covered

### 1. NumPy Fundamentals
- **Why NumPy?**: Provides n-dimensional array objects (`ndarray`) that operate significantly faster than standard Python lists through vectorized arithmetic and contiguous memory allocation.
- **Array Creation**: Creating 1D and 2D arrays using `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, and `np.random`.
- **Indexing & Slicing**: Row/column slicing, 2D matrix subsetting, and boolean masking for data filtering.
- **Vectorized Operations**: Fast element-wise operations (`+`, `-`, `*`, `/`, `**`) and matrix dot products (`np.dot`).
- **Statistical Operations**: Aggregating data with `np.sum`, `np.mean`, `np.median`, `np.std`, `np.max`, `np.min`, `np.argmax`, and axis-level operations (`axis=0` vs `axis=1`).
- **Reshaping & Manipulation**: `reshape()`, `transpose` (`.T`), and `flatten()`.

### 2. Pandas Basics
- **Data Structures**:
  - `pd.Series`: 1-dimensional labeled array.
  - `pd.DataFrame`: 2-dimensional tabular data structure with labeled axes (rows & columns).
- **Data I/O & Exploration**: Loading CSV files with `pd.read_csv()`, inspecting structure via `.head()`, `.tail()`, `.shape`, `.info()`, `.dtypes`, and `.describe()`.
- **Selection & Subsetting**: Selecting columns (`df['col']`), rows via `.iloc[]` (integer-location) and `.loc[]` (label-location).
- **Data Filtering**: Filtering rows based on single and multiple boolean conditions (`&`, `|`).
- **Handling Missing Values**: Detecting nulls using `isna()`, counting with `isna().sum()`, and imputing values using `.fillna()`.
- **Aggregation & Grouping**: Grouping data using `.groupby()` to calculate aggregated metrics.

---

## Repository & Folder Structure

```
Day 6/
│
├── student_performance.csv             # Input CSV Dataset (20 Student Records)
├── analyzed_student_performance.csv    # Exported Processed Dataset (with Totals, %, Grade, Status)
├── numpy_practice.py                   # Script 1: NumPy Exercises
├── pandas_practice.py                  # Script 2: Pandas Exploration
├── student_performance_analysis.py     # Mini Project: Student Performance Analysis
└── README.md                           # Documentation & Insights Report
```

---

## Practice Scripts & Mini Project Details

### 1. NumPy Practice Script ([numpy_practice.py](file:///d:/MLB-Internship/Day%206/numpy_practice.py))
- Demonstrates creation of 1D and 2D matrices.
- Demonstrates vectorized element-wise math and dot products.
- Demonstrates statistical aggregations across rows (`axis=1`) and columns (`axis=0`).
- Demonstrates array reshaping from 1D to 3x4 and 2x6, matrix transposition, and flattening.

### 2. Pandas Practice Script ([pandas_practice.py](file:///d:/MLB-Internship/Day%206/pandas_practice.py))
- Demonstrates Series and DataFrame instantiation.
- Reads `student_performance.csv` and outputs summary statistics.
- Filters dataset based on custom criteria (e.g. Python score >= 85, AI students with attendance >= 90%).
- Demonstrates handling missing data with mean imputation.

### 3. Student Performance Analysis Mini Project ([student_performance_analysis.py](file:///d:/MLB-Internship/Day%206/student_performance_analysis.py))
- **Data Ingestion**: Loads student performance CSV file.
- **Subject Analysis**: Computes mean, highest, and lowest scores for Python, Math, Statistics, and Machine Learning.
- **Feature Engineering**: Calculates Total Marks (out of 400), Percentage, Letter Grade (`A+`, `A`, `B`, `C`, `F`), and Performance Status (`Above Average` vs `Below Average`).
- **Top Performers & At-Risk Identification**: Finds Top 5 students and isolates students scoring below class average.
- **Program Performance**: Aggregates metrics by Academic Program (`AI`, `DS`, `SE`).
- **Export**: Writes computed fields back into `analyzed_student_performance.csv`.

---

## Key Insights Found From `student_performance.csv` Analysis

1. **Overall Performance**:
   - Class average percentage across all 20 students is **~80.44%**.
   - Top student in the batch is **Laiba Khan (SE)** with a **98.25%** average score (Total Marks: 389/400).
   - Top 5 students: **Laiba Khan (SE)**, **Ayesha Malik (SE)**, **Noor Fatima (SE)**, **Ahmed Raza (SE)**, and **Zainab Iqbal (AI)**.
2. **Subject Performance**:
   - **Machine Learning** and **Statistics** recorded the highest average scores (~81.2% and ~80.6% respectively).
   - **Mathematics** had the lowest average score (~79.1%), indicating an opportunity for targeted math review modules.
3. **Academic Program Comparison**:
   - **Software Engineering (SE)** students achieved the highest average percentage (**89.1%** average score, average attendance **93.5%**).
   - **Artificial Intelligence (AI)** students averaged **80.3%**.
   - **Data Science (DS)** students averaged **71.8%**, with attendance averaging **84.8%**, showing a positive correlation between attendance and final marks.

---

## Challenges Faced & Solutions

1. **Missing Data Handling & Type Safety**:
   - **Challenge**: Raw datasets can contain `NaN` or missing entries causing calculation errors.
   - **Solution**: Used Pandas `.isna().sum()` to verify dataset completeness and implemented `.fillna(df['col'].mean())` for numerical imputation.

2. **Axis Understanding in NumPy & Pandas**:
   - **Challenge**: Confusing `axis=0` (columns / vertical operation) vs `axis=1` (rows / horizontal operation).
   - **Solution**: Remembered that `axis=0` collapses rows to operate down columns (e.g. subject averages), while `axis=1` collapses columns to operate across rows (e.g. total student marks).

3. **Chained Indexing & SettingWithCopyWarning in Pandas**:
   - **Challenge**: Modifying subset DataFrames directly triggers warnings or unexpected copy behavior.
   - **Solution**: Used explicit `.copy()` when creating subset DataFrames or new calculated columns.

---

## How to Run the Scripts

### 1. Run NumPy Practice
```bash
python "Day 6/numpy_practice.py"
```

### 2. Run Pandas Practice
```bash
python "Day 6/pandas_practice.py"
```

### 3. Run Student Performance Analysis Mini Project
```bash
python "Day 6/student_performance_analysis.py"
```
