import pandas as pd

df = pd.read_csv(r"bitCoin/data_to_use/elliptic_txs_classes(1).csv")
df2 = pd.read_csv(r"bitCoin/data_to_use/elliptic_txs_edgelist(1).csv")
label = df["class"]
print(label.unique())
print(df.columns)
print(df[:-100])
print(df2)