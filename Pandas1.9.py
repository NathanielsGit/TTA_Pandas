#Is there a correlation between number of all-inclusive hotels and score?
import pandas as pd
df = pd.read_csv("pandatask.csv")
print (df)
import matplotlib.pyplot as plt

plt.matshow(df.corr())
plt.show()