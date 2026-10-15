import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import mean_absolute_error, accuracy_score

df = pd.DataFrame({
    "distance": [1,2,3,4,5,6,2,7,3,8,4,9,5,6,1,7],
    "traffic":  [1,1,2,2,3,3,1,3,2,3,2,3,1,2,1,2],
    "rain":     [0,0,0,1,1,1,0,1,0,1,0,1,1,0,1,0],
    "minutes":  [12,15,22,28,35,42,16,48,24,55,29,60,32,38,18,45]
})

df["late"] = (df["minutes"] > 35).astype(int)
print(df)