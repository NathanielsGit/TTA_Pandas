#Find the mean number of all-inclusive hotels across all destinations.

import pandas as pd

df = pd.read_csv("pandatask.csv")

print (df)

df_mean = df["Hotels"].mean()

print (df_mean)