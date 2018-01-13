from pandas import Series
from pandas import DataFrame

array = [1, 3, 5, 7, 9]

# define a series from an array
s1 = Series(array, index=['a', 'b', 'c', 'd', 'e'])

s2 = Series(array, index=['b', 'c', 'd', 'e', 'f'])

# automatic alignment
print(s1 + s2)

# define from dictionary(with index)
dic = {'a': 1, 'b': 3, 'c': 4, 'd': 5, 'e': 6}
s3 = Series(dic)
print(s3)

# drop function will return a new Series
s4 = s3.drop('a')
print(s4)

# select by index
s5 = s3[['a', 'b']]
print(s5)

# select by condition
s6 = s3[s3 >= 4]
print(s6)

# slice
s7 = s3[:2]
s7 = s3['b':'e']
print(s7)

# create a DataFrame form Series
df = DataFrame({"series1": s3, "series2": s7})
print(df)


