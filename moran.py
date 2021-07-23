# coding=utf-8
import pandas as pd
import numpy as np


# 调整列顺序
# df = pd.read_excel('距离矩阵.xlsx')
# t = df.columns.values.tolist()
# t.remove('ID')
# t.sort()
# tmp = []
# for i in t:
#     tmp.append(df[i].values)

# d = dict(zip(t, tmp))

# distance = pd.DataFrame(d)
# distance.to_excel('test.xlsx')

df = pd.read_excel('距离矩阵.xlsx')
mat = np.zeros((157, 157))
for i in range(157):
    for j in range(157):
        mat[i, j] = df.loc[i].values[j+1]

distance_mat = 1.0 / mat
for i in range(157):
    print(distance_mat[i, :])
    






