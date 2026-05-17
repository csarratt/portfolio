import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "region": ["Northeast", "Midwest", "South", "West"],
    "annual_childcare_cost": [15200, 11800, 10300, 16750]
})

plt.figure(figsize=(8, 5))
plt.bar(data["region"], data["annual_childcare_cost"])
plt.title("Annual Childcare Cost by Region")
plt.xlabel("Region")
plt.ylabel("Annual Cost")
plt.tight_layout()
plt.savefig("childcare_costs.png")

print("Childcare Visualization Demo")
print("Saved chart as childcare_costs.png")
print(data)
