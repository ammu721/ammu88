import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
data=pd.read_csv(r'C:\Users\hp\Salary_Data.csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,1].values
from sklearn.linear_model import LinearRegression
lin_regs=LinearRegression()
lin_regs.fit(x,y)
from sklearn.preprocessing import PolynomialFeatures
poly_reg=PolynomialFeatures(degree=2)
x_poly=poly_reg.fit_transform(x)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(x,y,color='blue')
plt.plot(x,lin_regs.predict(x),color='red')
plt.title('bluff detection model(Linear regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()
plt.scatter(x,y,color='green')
plt.plot(x,lin_reg2.predict(x_poly),color='black')
plt.title('bluff detection model(polynomial regression)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()