import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(5),
               index= pd.date_range('20200301',periods=5)) #頻率為日
print(ts)
print('')

ts = pd.Series(np.random.randn(5),
               index= pd.date_range('20200301 12:59:30',periods=5)) #頻率為日
print(ts)
print('')

ts = pd.Series(np.random.randn(5),
               index= pd.date_range('2020-03-01',periods = 5,freq = '1h5min')) #頻率為65T (65分鐘)
print(ts)
print('')


ts = pd.Series(np.random.randn(5),
               index= pd.date_range('2020-02-01',periods=5, freq='M')) #頻率為月,顯示每個月最後一天
print(ts)
print('')

ts = pd.Series(np.random.randn(5),
               index= pd.date_range('2020/03/02',periods=5, freq='W')) #頻率為周
print(ts)
print('')




