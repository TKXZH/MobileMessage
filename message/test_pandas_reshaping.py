import pandas as pd

df = pd.read_csv('/Users/zonghuixu/Downloads/roq_result (7).csv')

# 按照某列的值排序
df_roq_order = df.sort_values('roq', ascending=False)
print(df_roq_order.head())

# 重命名列名
df_roq_rename = df.rename(columns={'roq': 'ROQ'})
print(df_roq_rename.columns)

df.plot.scatter(x='sku', y='roq')