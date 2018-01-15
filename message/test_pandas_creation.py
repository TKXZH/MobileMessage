import pandas as pd
import numpy as np

'''
创建DataFrame
'''
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

'''
查看DataFrame
'''
# View Data
# 取前n行
print(df.head(3))

# 查看index, columns, values
print(df.index)
print(df.columns)
print(df.values)

# 查看summary
print(df.describe())

# 转置
print(df.T)

# 排序(根据index或者column, axis为0表示横向, 1表示纵向)
print(df.sort_index(axis=0, ascending=False))

# 排序(根据values)
print(df.sort_values(by='A', ascending=False))

'''
查询DataFrame
'''
# 根据列名选择一列
print(df['A'])

# 切片选择多行
print(df[:2])

# 根据index选择多行
print(df['20130102':'20130103'])

# 在不同维度进行选择
print(df.loc["20130101", ['A', 'B']])

# 根据位置选择
print(df.iloc[:, 2:5])

# 过滤
print(df[df.A > 0])
print(df[df > 0])

df2 = df.loc[:, :]
df2['E'] = ['one', 'one','two','three','four','three']
print(df2[df2.E.isin(['one', 'two'])])

'''
写入DataFrame
'''
# 增加一列
s1 = pd.Series(list('123456'), index=pd.date_range('20130102', periods=6))
df['F'] = s1

# 根据label设
df.loc[dates[0], 'A'] = 0

# 根据位置设值, 自动对齐
df.iloc[0, 1] = 0
df.loc[:, 'D'] = 5
print(df)


