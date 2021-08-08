#How many rows and columns are there in your file?

import pandas as pd

df = pd.read_csv("pandatask.csv")

print (df)

df.info()