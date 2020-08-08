import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,100,24).reshape(6,4),columns=list('ABCD'))
print(df)
print('')

print(df.head(3))  #取得前三列
print('')

print(df.tail(2)) #取得後二列
print('')

print(df.describe()) #基本運算: 平均 標準差 最小 中位數 最大
print('')

df['TAG'] = ['M','F','F','M','F','M']  #加入標籤
print(df)
print('')

#設定浮點數顯示方式
pd.options.display.float_format = '{:,.0f}'.format

print(df.groupby('TAG').sum()) #分組累計
print('')

print(df.groupby('TAG').mean()) #分組平均
print('')




