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
