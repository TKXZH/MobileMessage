from pandas import Series

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

