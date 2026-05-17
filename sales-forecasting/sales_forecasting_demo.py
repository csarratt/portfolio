import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=365, freq="D")
sales = (
    200
    + 20 * np.sin(2 * np.pi * dates.dayofyear / 365)
    + dates.dayofweek * 3
    + np.random.normal(0, 10, len(dates))
)

df = pd.DataFrame({"date": dates, "sales": sales})
df["day_of_week"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month
df["day_of_year"] = df["date"].dt.dayofyear

X = df[["day_of_week", "month", "day_of_year"]]
y = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
rmse = mean_squared_error(y_test, predictions) ** 0.5

results = pd.DataFrame({
    "actual_sales": y_test.values[:10],
    "predicted_sales": predictions[:10]
})

print("Sales Forecasting Demo")
print(f"RMSE: {rmse:.2f}")
print("\nSample predictions:")
print(results)
