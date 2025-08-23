import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import mlflow
import mlflow.sklearn
import pickle

train = pd.read_csv('Iris.csv')
feature_cols = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

X = train[feature_cols]
y = train['Species']

enc = LabelEncoder()
y = enc.fit_transform(y.values)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3, shuffle=True)
pd.concat([X_train, pd.DataFrame(y_train)], axis=1).to_csv('train.csv', index=False)
pd.concat([X_test, pd.DataFrame(y_test)], axis=1).to_csv('test.csv', index=False)