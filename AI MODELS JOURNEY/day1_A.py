import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "student": ["A","B","C","D","E"],
    "study_hours": [1, 2, 3, 4, 5],
    "attendance": [90,85,80,75,70],
    "assignments": [2,3,4,5,6],
    "marks": [60,70,80,90,100]
}

df = pd.DataFrame(data)
print(df)

print("1st 5 rows:\n",df.head(5))

print("\nLast 3 rows:\n",df.tail(3))

print("\nRows & Columns:\n", df.shape)

print("\nColumn names:\n", df.columns.tolist())


print("Mean:\n", df["marks"].mean())

print("Median:\n", df["marks"].median())

print("Minimum:\n", df["marks"].min())

print("Maximum:\n", df["marks"].max())

result = df[df["marks"]>70]

print(result)  

sorted_data = df.sort_values(by="marks",ascending=False)

print(sorted_data)

df["study_category"] = np.where(
    df["study_hours"]>3,
    "High",
    "Low"
)

print(df[["student", "study_hours", "study_category"]])

hours = np.array(df["study_hours"])

print("Array:\n", hours)

print("Shape:\n", hours.shape)

print("Data type:\n", hours.dtype)

print("After adding 2:\n", hours + 2)

a = df["study_hours"]

normalized = (a - a.min()) / (a.max() - a.min())

print("Normalized:\n", normalized)
