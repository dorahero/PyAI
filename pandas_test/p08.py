import pandas as pd

df = pd.read_csv('https://bit.ly/uforeports')

print(df.columns)
print('')

#['City', 'Colors Reported', 'Shape Reported', 'State', 'Time']

print(df.count()) #每個欄位累計筆數 不含NAN
print('')

df1 =df[df.City.isnull()]
print(df1)  #列出City缺值的資料
print('')

print(len(df1)) #列出City缺值的列數
print('')

df = pd.read_csv('https://bit.ly/uforeports', usecols=[0,3,4])

print(df.head(5))


