import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "student": ["A","B","C","D","E"],
    "study_hr": [1, 2, 3, 4, 5],
    "attendance": [90,85,80,75,70],
    "assignments": [2,3,4,5,6],
    "marks": [60,70,80,90,100]
}

df = pd.DataFrame(data)
print(df)
