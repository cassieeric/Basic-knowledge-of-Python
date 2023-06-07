import numpy as np
import pandas as pd

df1 = pd.DataFrame({"姓名": ["张剑", "李红", "王帅"], "科目1成绩": [95, np.NAN, 89], "科目2成绩": [90, 85, np.NAN]})
# df2 = df1.dropnav()
df3 = df1[df1["科目1成绩"] != np.NAN]
print(df3)




