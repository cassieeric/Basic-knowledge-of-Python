import numpy as np
import pandas as pd

df1 = pd.DataFrame({"姓名": ["张剑", "李峰", "王帅"], "成绩": [95, 98, 89]})
df2 = pd.DataFrame({"姓名": ["张剑", "李红", "王帅"]})
df = pd.merge(df2, df1, on="姓名", how="left")
df = df.fillna(0)  # 使用填充的方法进行删除
print(df)


