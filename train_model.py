import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import mlflow
import mlflow.sklearn
import pickle
def main():
    train = pd.read_csv('Iris.csv')
    feature_cols = ['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']

    X = train[feature_cols]
    y = train['Species']

    enc = LabelEncoder()
    y = enc.fit_transform(y.values)
    print(len(y))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3, shuffle=True)
    mlflow.set_experiment('iris')

    with mlflow.start_run():
        n_estimators = 100
        max_depth = 1000
        min_samples_split = 2
        min_samples_leaf = 5
        random_state = 3
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            random_state=3)
        model.fit(X_train, y_train)
        accuracy = accuracy_score(y_test, model.predict(X_test))
        mlflow.log_param("model_type", 'RandomForest')
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_param("min_samples_split", min_samples_split)
        mlflow.log_param("min_samples_leaf", min_samples_leaf)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "model")

        mlflow.log_param('train_size', len(X_train))
        mlflow.log_param('test_size', len(X_test))
        with open('model_weights/model.pkl', 'wb') as f:
            pickle.dump(model, f)

        print(f"Accuracy: {accuracy:.4f}")
