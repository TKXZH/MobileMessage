import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv('/Users/zonghuixu/Downloads/roq_result (7).csv', header=0)
# dflow = df[df.logicRoqResult > 10000]

df1 = pd.DataFrame({'sku': {"line1": 23, "line2": 333, "line3": 56}, 'roq': {"line1": 334, "line2": 123, "line3": 555}})

df2 = pd.DataFrame([{"sku": 23, "roq": 334}, {"sku": 333, "roq": 123}, {"sku": 56, "roq": 55}])


s = pd.Series([1,'asda',234,5456,'A'])
print(s)