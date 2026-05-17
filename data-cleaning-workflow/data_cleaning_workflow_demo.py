import pandas as pd

raw_data = pd.DataFrame({
    "customer_name": [" Alice Smith ", "bob jones", None, "  Maria Garcia"],
    "purchase_amount": [120.50, None, 75.00, 210.25],
    "state": ["tx", "TX", "ca", None]
})

cleaned = raw_data.copy()
cleaned["customer_name"] = cleaned["customer_name"].fillna("Unknown").str.strip().str.title()
cleaned["purchase_amount"] = cleaned["purchase_amount"].fillna(cleaned["purchase_amount"].median())
cleaned["state"] = cleaned["state"].fillna("Unknown").str.upper()
cleaned["high_value_purchase"] = cleaned["purchase_amount"] >= 150

print("Data Cleaning Workflow Demo")
print("\nRaw data:")
print(raw_data)

print("\nCleaned data:")
print(cleaned)
