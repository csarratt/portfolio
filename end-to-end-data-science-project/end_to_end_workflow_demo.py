import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

np.random.seed(42)

df = pd.DataFrame({
    "engagement_score": np.random.randint(1, 100, 400),
    "days_since_last_activity": np.random.randint(0, 60, 400),
    "completed_profile": np.random.choice([0, 1], 400)
})

df["target_success"] = (
    (df["engagement_score"] > 55) &
    (df["days_since_last_activity"] < 25) &
    (df["completed_profile"] == 1)
).astype(int)

X = df[["engagement_score", "days_since_last_activity", "completed_profile"]]
y = df["target_success"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.25)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("End-to-End Data Science Workflow Demo")
print(f"Model accuracy: {accuracy:.2%}")
print("\nRecommendation:")
print("Users with high engagement, recent activity, and completed profiles are more likely to succeed.")
