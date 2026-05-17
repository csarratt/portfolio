import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

data = pd.DataFrame({
    "group": ["Control", "Variant"],
    "visitors": [8000, 8050],
    "conversions": [816, 912]
})

data["conversion_rate"] = data["conversions"] / data["visitors"]

control_rate = data.loc[data["group"] == "Control", "conversion_rate"].iloc[0]
variant_rate = data.loc[data["group"] == "Variant", "conversion_rate"].iloc[0]
lift = (variant_rate - control_rate) / control_rate

count = data["conversions"].values
nobs = data["visitors"].values
z_stat, p_value = proportions_ztest(count, nobs)

print("A/B Testing Analysis Demo")
print(data)
print(f"\nLift: {lift:.2%}")
print(f"Z-statistic: {z_stat:.3f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Recommendation: The variant shows a statistically significant difference.")
else:
    print("Recommendation: The result is not statistically significant.")
