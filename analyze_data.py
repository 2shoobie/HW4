import pandas as pd

df = pd.read_csv("data/StudentExam.csv")

print("\n First 5 rows of the DataFrame:")
print(df.head())

print("DataFrame Info:")
print(df.info())

print("\n Summary Statistics:")
print(df.describe())
# 2  
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
# 3
print ("\n Students with reading score greater than 90:")
high_reading = df[df["reading score"] > 90]
print(high_reading)

print("\n Male students with reading score less than 50:")
male_reading_level = df[(df["reading score"] < 50) & (df["Gender"] == "male")]
print(male_reading_level.head())
# 4
print("\n Average score:")
df["Average score"] = df[["math score", "reading score", "writing score"]] / 3
print(df[["reading score", "math score", "writing score"]].head())

print("reading score Drop Column:")
df = df.drop("reading score", axis=1)
print("\nCurrent Columns:")
print(df.columns)
# 5
print("Average writing score by gender:")
gender_scre = df.groupby("Gender")["writing score"].mean()
print(gender_scre)

