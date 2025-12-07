#Name: Solii.M
#Date: 12/5/25
# Homework 4: Student Exam Data Analysis
#Prof:I, INST326

"""
The file is a script reading a student exam CSV file with the help of pandas and providing simple data analysis.
It gives the initial rows of the data, summary data and statistics. Creation and dropping of a column, and groupby to determine the average score of the gender.
All the findings are printed on the console.
"""
import pandas as pd
#1 Data Loading 
df = pd.read_csv("data/StudentExam.csv")

print("\n First 5 rows of the DataFrame:")
print(df.head())

print("DataFrame Info:")
print(df.info())

print("\n Summary Statistics:")
print(df.describe())
# 2  Indexing and Selection
print("2: A single row by its position")
print(df.iloc[0])

print("\n Slice of rows from index 2 to 5:")
print(df.iloc[2:5])

print("\n Slice of rows by positions 1, 3, and 4:")
print(df.iloc[[1, 3, 4]])

print("\n Single column by name: 'reading score'")
print(df["reading score"].head())

print("\n Single cell with loc[0, 'reading score']")
print(df.loc[0, "reading score"])
# 3 Filtering
print ("\n Students with reading score greater than 90:")
high_reading = df[df["reading score"] > 90]
print(high_reading)

print("\n Male students with reading score less than 50:")
male_reading_level = df[(df["reading score"] < 50) & (df["gender"] == "male")]
print(male_reading_level.head())
# 4 Droping and Creating Columns
print("\n average score:")
df["average score"] = df[["math score", "reading score", "writing score"]].mean(axis=1) /3
print(df[["reading score", "math score", "writing score"]].head())

print("reading score Drop Column:")
df = df.drop("reading score", axis=1)
print("\nCurrent Columns:")
print(df.columns)
# 5 GroupBy Operations
print("average writing score by gender:")
gender_scre = df.groupby("gender")["writing score"].mean()
print(gender_scre)

