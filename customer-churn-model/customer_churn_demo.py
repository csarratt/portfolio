import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

np.random.seed(42)

n = 500
df = pd.DataFrame({
    "monthly_spend": np.random.normal(75, 20, n),
    "support_tickets": np.random.poisson(1.5, n),
    "months_active": np.random.randint(1, 48, n)
})

df["churn"] = (
    (df["support_tickets"] > 2) |
    (df["months_active"] < 6) |
    (df["monthly_spend"] < 45)
).astype(int)

X = df[["monthly_spend", "support_tickets", "months_active"]]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.25)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Customer Churn Model Demo")
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
print(classification_report(y_test, predictions))
