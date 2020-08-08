import pandas as pd

s = pd.Series([3,5,6,0,2])
print(s)
print('')

s = pd.Series([3,5,6,0,2] ,index=range(20,25))
print(s)
print('')

s = pd.Series([3,5,6,0,2] ,index=['a','b','c','d','e'])
print(s)
print('')

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)
print('')

s = pd.Series(data,index=['b','a','d','c'])
print(s)
print(s['b'])


