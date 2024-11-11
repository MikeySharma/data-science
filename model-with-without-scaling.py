import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()
df = pd.read_csv('cars2.csv')
X = df.drop(['Car', 'Model', 'CO2'], axis=1)

#Overwriting X by Scaling it
X = scale.fit_transform(X)

y = df['CO2']


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
