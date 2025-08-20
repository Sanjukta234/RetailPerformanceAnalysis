# Retail Inventory Turnover Analysis
# Author email: 22f1001636@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt

TARGET = 8.0

# Load data
df = pd.read_csv("inventory_turnover_2024.csv")

# Compute average (should be 4.88 per prompt)
avg = round(df["InventoryTurnover"].mean(), 2)
print("Average Inventory Turnover (2024):", avg)

# Plot trend line
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["InventoryTurnover"], marker="o")
plt.axhline(TARGET, linestyle="--")
plt.title("Inventory Turnover Ratio – 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Inventory Turnover Ratio")
plt.tight_layout()
plt.savefig("turnover_trend.png", dpi=150)
plt.close()

# Plot bars
plt.figure(figsize=(8, 5))
plt.bar(df["Quarter"], df["InventoryTurnover"])
plt.axhline(TARGET, linestyle="--")
plt.title("Inventory Turnover Ratio by Quarter vs Target")
plt.xlabel("Quarter")
plt.ylabel("Inventory Turnover Ratio")
plt.tight_layout()
plt.savefig("turnover_bars.png", dpi=150)
plt.close()
