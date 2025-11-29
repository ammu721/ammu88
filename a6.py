import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt 
data=pd.read_csv(r'C:\Users\hp\iris.csv')
df=pd.DataFrame(data)
df.columns=['sepal.length','sepal.width','petal.length','petal.width','species']
print(df.head())
from pandas.api.types import is_numeric_dtype 
for col in df.columns:
    if is_numeric_dtype(df[col]):
        print('%s'%(col))
        print('mean=%.3f'%df[col].mean())
        print('std=%.3f'%df[col].std())
        print('min=%.3f'%df[col].min())
        print('max=%.3f'%df[col].max())
numeric_columns=df.select_dtypes(include='number').columns
print(numeric_columns)
covariance_series=df[numeric_columns].cov()['sepal.length']
for covariance,value in covariance_series.items():
    print(f'{covariance}:{value:.2f}')
data['sepal.length'].hist(bins=8)
data.boxplot()
plt.show()
