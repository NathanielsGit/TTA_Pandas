#Find the highest scoring destination.
import pandas as pd
df = pd.read_csv("pandatask.csv")
print (df)
df_max = df["Rating"].max()
df_loc = df.loc[df['Rating'] == df_max]
print('\nResult - Highest Ratings Score location :\n', df_loc)