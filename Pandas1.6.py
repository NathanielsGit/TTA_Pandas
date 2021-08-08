#Find all the destinations where there are more than 9 all-inclusive hotels.
import pandas as pd
df = pd.read_csv("pandatask.csv")
print (df)
df_loc = df.loc[df["Hotels"] > 9]
print('\nResult - Locations with more than 9 all inclusive hotels :\n', df_loc)