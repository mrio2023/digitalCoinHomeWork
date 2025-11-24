import pandas as pd
import os

# 1. 读
df = pd.read_csv(r"bitCoin\data_to_use\AddrAddr_edgelist.csv")

# 2. 删第一列
df = df.drop(df.columns[0], axis=1)

# 3. 写到临时文件（或直接覆盖但加 index=False）
tmp = r"bitCoin/data_to_use/AddrAddr_edgelist_new.csv"
df.to_csv(tmp, index=False)          # 关键：不要写索引
os.replace(tmp,                      # 原子替换
           r"bitCoin/data_to_use/AddrAddr_edgelist.csv")

# 4. 重新读验证
df_check = pd.read_csv(r"bitCoin/data_to_use/AddrAddr_edgelist.csv")
print(df_check.head())