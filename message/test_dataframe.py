from pandas import DataFrame
from pandas import Series

# 1. create DataFrame from [[]]
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]
array = [array1, array2]
df1 = DataFrame(array, index=["line1", "line2"], columns=["column1", "column2", "column3", "column4", "column5"])
print(df1)

# 2. create DataFrame from {[]}
dic1 = {"column1": [1, 6], "column2": [2, 7], "column3": [3, 8], "column4": [4, 9], "column5": [5, 10]}
df2 = DataFrame(dic1)
print(df2)

# 3. create DataFrame from {{}}
dic2 = {"column1": {"line1": 1, "line2": 6}, "column2": {"line1": 2, "line2": 7}, "column3": {"line1": 3, "line2": 8},
        "column4": {"line1": 4, "line2": 9}, "column5": {"line1": 5, "line2": 10}}
df3 = DataFrame(dic2)
print(df3)