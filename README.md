# Student Performance Analytics

## Description

A command-line Student Performance Analytics application built with Python and Pandas that allows users to load student datasets and perform comprehensive performance analysis. The application provides dataset inspection, data cleaning, descriptive statistics, subject-wise analysis, filtering, sorting, grouping, performer identification, and CSV exporting through an interactive CLI.

---

## Features

- Load student datasets from CSV files
- Display dataset overview
  - Number of rows
  - Number of columns
  - Data types
  - Duplicate row count
- Clean datasets
  - Remove missing values
  - Replace missing values with zero
  - Preserve original dataset
- Generate descriptive statistics
- Generate column-wise statistics
- Generate subject-wise statistics
- Filter students by column values
- Sort dataset
  - By index
  - By column values
- Calculate overall dataset statistics
  - Mean
  - Median
  - Sum
- Group and summarize data
- Identify student performers
  - Highest scorer
  - Lowest scorer
  - Students above a threshold
  - Students below a threshold
- Export processed datasets to CSV
- Input validation and error handling

---

## Technologies

- Python
- Pandas

---

## Concepts Practiced

- DataFrames and Series
- CSV File Handling
- Data Cleaning
- Missing Value Handling
- Descriptive Statistics
- Boolean Indexing
- Filtering Data
- Sorting Data
- GroupBy Operations
- Aggregate Functions
- Data Export
- Exception Handling
- Modular Programming
- CLI Application Development

---

## Project Structure

```text
Student Performance Analytics/
│
├── main.py
├── analytics.py
├── students.csv
└── README.md
```

---

## How to Run

Clone the repository.

```bash
git clone https://github.com/VaibhavKumar777/Student-Performance-Analytics
```

Navigate to the project folder.

```bash
cd Student-Performance-Analytics
```

Install Pandas.

```bash
pip install pandas
```

Run the application.

```bash
python main.py
```

---

## Sample Dataset

```csv
Student_ID,Name,Section,Gender,Math,Physics,Chemistry,English,Attendance
S001,Aarav,A,Male,92,88,91,85,95
S002,Diya,A,Female,81,79,84,90,91
S003,Rohan,B,Male,67,72,69,75,88
S004,Ananya,B,Female,95,98,97,96,99
S005,Vivaan,C,Male,54,61,58,65,80
S006,Meera,C,Female,88,85,90,89,94
S007,Kabir,A,Male,76,70,74,72,87
S008,Ishita,B,Female,91,93,92,95,97
S009,Arjun,C,Male,45,52,,60,70
S010,Saanvi,A,Female,83,86,84,,93
S011,Krish,B,Male,78,81,79,80,89
S012,Aadhya,C,Female,97,96,98,99,100
S013,Rudra,A,Male,62,58,60,64,82
S014,Kiara,B,Female,89,87,91,88,96
S015,Yash,C,Male,71,74,70,73,85
S016,Tara,A,Female,84,82,85,86,92
S017,Dev,B,Male,58,55,57,59,78
S018,Myra,C,Female,93,94,92,95,98
S019,Aditya,A,Male,66,68,70,67,84
S020,Siya,B,Female,87,90,89,91,95
S020,Siya,B,Female,87,90,89,91,95
```

---

## Future Improvements

- Support multiple filtering conditions
- Advanced filtering using comparison operators (`>`, `<`, `>=`, `<=`)
- Allow custom aggregation functions for grouped analysis
- Generate summary reports
- Data visualization with Matplotlib
- Support Excel and JSON datasets
- Interactive performance dashboards

---

## Time Taken

Approximately **125 minutes**

---

## Author

**Vaibhav Kumar**