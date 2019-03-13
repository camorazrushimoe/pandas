import pandas as pd
import numpy as np

# len 3 596 463
df = pd.read_csv('test_data.csv', header=0)
df.sort_values(by=['timestamp'])

print(df.dtypes)

all_budget = 1000000
df['threshold'] = df["alpha"]
df.loc[df["threshold"] < 0, "threshold"] = 0
df.loc[df["threshold"] > 0, "threshold"] = 1
df.loc[df["threshold"] > 0, "count"] = all_budget / df["ask"]
df['budget'] = all_budget

df2 = df[0:20]

print(df2)
print(df2.plot)

