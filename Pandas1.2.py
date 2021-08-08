#Print row 3-8 ( using iloc/loc).

import pandas as pd

df = pd.read_csv("pandatask.csv")

print (df)

print (df.iloc[3:8])