import pandas as pd

optimizely = pd.DataFrame({
    "visitor_id": [101, 102, 103, 104, 105],
    "variation": ["Control", "Variant", "Variant", "Control", "Variant"]
})

analytics = pd.DataFrame({
    "visitor_id": [101, 102, 103, 104, 105],
    "reported_variation": ["Control", "Variant", "Control", "Control", "Variant"]
})

merged = optimizely.merge(analytics, on="visitor_id")
merged["match"] = merged["variation"] == merged["reported_variation"]

mismatches = merged[~merged["match"]]

print("Experiment Attribution Optimization Demo")
print("\nMerged tracking records:")
print(merged)

print("\nMismatched records:")
print(mismatches)
