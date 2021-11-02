from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

dataset = pd.read_csv('data.csv')
print(dataset)
x = dataset.iloc[: , :-1].values
y = dataset.iloc[: , -1].values
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=142)
print(x_train)
print(x_test)
print(y_train)
print(y_test) 


from sklearn.linear_model import LinearRegression
regresor = LinearRegression(x , y)
regresor.fit(x_train, y_train)

plt.pyplot(x_train, x_test, y_train, y_test, colors='red')
plt.scatter(x, y_pred())
plt.xlabel('independent variable')
plt.ylabel('dependent variable')
plt.show()

