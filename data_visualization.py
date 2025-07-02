import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("simulated_tips_data.csv")  # Use the dataset you downloaded

# Step 2: Visualization 1 – Average Tip by Day
plt.figure(figsize=(8, 5))
sns.barplot(x="day", y="tip", data=df)
plt.title("Average Tip by Day")
plt.tight_layout()
plt.savefig("average_tip_by_day.png")
plt.close()

# Step 3: Visualization 2 – Tip vs Total Bill
plt.figure(figsize=(8, 5))
sns.scatterplot(x="total_bill", y="tip", hue="time", data=df)
plt.title("Tip vs Total Bill")
plt.tight_layout()
plt.savefig("tip_vs_bill.png")
plt.close()

print("✅ Charts saved: average_tip_by_day.png & tip_vs_bill.png")
