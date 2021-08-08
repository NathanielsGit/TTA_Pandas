#Find the lowest scoring destination.
import pandas as pd
df = pd.read_csv("pandatask.csv")
print (df)
df_min = df["Rating"].min()
df_loc = df.loc[df['Rating'] == df_min]
print('\nResult - Lowest Ratings score location :\n', df_loc)