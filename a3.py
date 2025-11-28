import pandas as pd  
df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['maths','java','python'])
print(df)
print(df.sum())
print(df.agg(['sum','count','std','var','size','min','max']))
print(df.describe())
a=df.groupby('java')
print(a.first())