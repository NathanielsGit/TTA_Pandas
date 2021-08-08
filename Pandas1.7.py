#Filter the data by score above 8.
import pandas as pd
df = pd.read_csv("pandatask.csv")
print (df)
df_loc = df.loc[df["Feedback"] > 8]
print('\nResult - Locations with Feedback score above 8  :\n', df_loc)