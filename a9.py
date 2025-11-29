import pandas as pd  
import matplotlib.pyplot as plt  
import numpy as np 
iris=pd.read_csv(r'C:\Users\hp\iris.csv')
fig=iris[iris.species=='setosa'].plot.scatter(x='petal.length',y='petal.width',color='orange',label='setosa')
iris[iris.species=='versicolor'].plot.scatter(x='petal.length',y='petal.width',color='green',label='versicolor',ax=fig)
iris[iris.species=='virginica'].plot.scatter(x='petal.length',y='petal.width',color='purple',label='virginica',ax=fig)
fig.set_xlabel('petal.length')
fig.set_ylabel('petal.width')
fig.set_title('petal length and width')
fig=plt.gcf()
fig.set_size_inches(5,5)
plt.show()
petal_width=iris[iris['petal.width']==1.4]
print(petal_width)
count=iris.groupby('petal.length')['petal.length'].count()
print(count)
sum=iris['petal.length'].sum()
print(sum)
max=iris['speal.width'].max()
print(max)
add=iris['speal.length']+1.0
print(add)