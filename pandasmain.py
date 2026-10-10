import pandas as pd

df = pd.read_csv("data/raw/pc_shipments.csv")

print(df)
print(df.shape)
df.info()