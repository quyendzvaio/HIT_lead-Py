import numpy as np
import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_absolute_error

MODEL_PATH = Path("../model/house_price_model.pkl")


def generate_data(n=500, seed=42):
    np.random.seed(seed)

    area = np.random.randint(30, 200, n)
    bedrooms = np.random.randint(1, 6, n)
    distance = np.random.uniform(1, 20, n)

    price = (
        50 * area
        + 200 * bedrooms
        - 30 * distance
        + np.random.normal(0, 1000, n)
    )

    return pd.DataFrame({
        "area": area,
        "bedrooms": bedrooms,
        "distance": distance,
        "price": price
    })


def train_and_evaluate(data: pd.DataFrame):
    X = data[["area", "bedrooms", "distance"]]
    y = data["price"]

    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.5, random_state=42
    )

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", SGDRegressor(
            early_stopping = True,
            loss="squared_error",
            learning_rate="constant",
            eta0=0.01,
            max_iter=1000,
            random_state=42
        ))
    ])

    model.fit(X_train, y_train)
    train_mae = mean_absolute_error(y_train,model.predict(X_train))

    val_mae = mean_absolute_error(y_val, model.predict(X_val))
    test_mae = mean_absolute_error(y_test, model.predict(X_test))

    return model, val_mae, test_mae,train_mae


def save_model(model):
    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)


def main():
    data = generate_data()
    model, val_mae, test_mae,train_mae = train_and_evaluate(data)
    print(f"TRAIN MAE: {train_mae:.2f}")

    print(f"VAL MAE : {val_mae:.2f}")
    print(f"TEST MAE: {test_mae:.2f}")

    save_model(model)
    print("Model saved to:", MODEL_PATH.resolve())


if __name__ == "__main__":
    main()
