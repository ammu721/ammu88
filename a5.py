import pandas as pd   
range_date=pd.date_range(start='1/9/2025',end='30/9/2025',freq='min')
print(range_date)
print(type([0]))

import numpy as np 
range_date=pd.date_range(start='1/9/2025',end='30/9/2025',freq='min')
df=pd.DataFrame(range_date,columns=['date'])
df['date']=np.random.randint(0,100,size=(len(range_date)))
string_data=[str(x) for x in range_date]
print(string_data[1:11])
