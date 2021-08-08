#Filter the data score below 2 ( I need to know if these destinations should be
import pandas as pd
df = pd.read_csv("pandatask.csv")
print (df)
df_loc = df.loc[df["Feedback"] < 2]
print('\nResult - Locations with Feedback score less than 2  :\n', df_loc)