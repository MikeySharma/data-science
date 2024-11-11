import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error



df = pd.read_csv('./data-sets/housing.csv')
df = df.dropna()
df['ocean_proximity'].replace(['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'], [0, 1, 2, 3, 4], inplace=True)
# print(df.head())
x = df.drop(['median_house_value'], axis=1)
y = df['median_house_value']

print(df.corr())
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

r2Score = r2_score(y_test, y_pred)


# plt.scatter(x_test, y_test)
# plt.scatter(x_test, y_pred, color='r')
# plt.title('Showing Training and Testing Data')
# plt.show()
print(f'R2 Score: {r2Score}')
