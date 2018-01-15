import pandas as pd

df = pd.read_csv("/Users/zonghuixu/Downloads/roq_result (7).csv")
print(df.describe())
print(df[["sku", "roq"]][1:1000])
print(df["roq"])
print(df[df["sku"] == 2122960][["sku", "fc", "roq"]])

# axis 为1表示按列删除，默认为0表示按行删除
df.drop("uuid", axis=1)

index = df[df["sku"] == 2122960].index
df.drop(index)

# 去重操作
df.drop_duplicates()
print(len(df))
print(df["sku"].nunique())
print(df[["sku", "fc"]].nunique())

df_sku_fc = df.groupby("sku").size().reset_index(name='num_fc')
print(df_sku_fc[df_sku_fc["num_fc"] > 2])

# group by
# df_fc_roq = df.groupby("fc").sum("roq")
# print(df_fc_roq)

# 根据roq对sku进行分级
level_list = list()
for i in df.index:
    roq = df.loc[i, "roq"]
    if roq > 1000:
        level = "super"
    elif 1000 >= roq >= 100:
        level = "large"
    elif 100 > roq > 1:
        level = "small"
    else:
        level = "little"

    level_list.append(level)

df["level"] = pd.Series(level_list)
print(df[df["level"] == "super"].tail())

df['score'] = df['roq'].map(lambda x: "good" if x > 100 else "bad")
print(df['score'])

# 按行索引数据
print(df.loc[0])
print(df.loc[[1, 3, 8]])

# 按列索引数据
print(df['roq'])
print(type(df['roq']))

# 按照行和列同时索引数据
print(df.loc[[1, 3, 4], ["sku", "roq"]])
print(type(df.loc[[1, 3, 4], ["sku", "roq"]]))

# 按条件进行筛选
print(df[(df['roq'] > 100) & (df['unit'].isin(['Pet']))][['sku', 'roq', 'unit']])
pet = df[(df['roq'] > 100) & (df['unit'].isin(['Pet']))][['sku', 'roq', 'unit']]
pet2 = df[df.unit == 'Pet']
print(pet2.head())
# 生成csv文件
# pet.to_csv(path_or_buf='./pet.csv', index=False)

# 查看各个列的数据类型
print(df.dtypes)

# 查看索引
print(df.index)

# 查看列名
print(df.columns)

# 产看行数和列数
print(df.shape)
