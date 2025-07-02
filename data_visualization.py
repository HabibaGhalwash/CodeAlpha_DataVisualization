import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
try:
    df = pd.read_csv("simulated_tips_data.csv")
    print(f"📄 Loaded 'simulated_tips_data.csv' with {len(df)} rows.")
except FileNotFoundError:
    print("❌ Error: 'simulated_tips_data.csv' not found.")
    exit()

# Step 2: Clean data (optional safety step)
df.dropna(inplace=True)

# Step 3: Visualization 1 – Average Tip by Day
plt.figure(figsize=(8, 5))
sns.barplot(x="day", y="tip", data=df, estimator='mean', errorbar=None)
plt.title("Average Tip by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Average Tip ($)")
plt.tight_layout()
plt.savefig("average_tip_by_day.png", dpi=300)
plt.close()
print("📊 Saved: average_tip_by_day.png")

# Step 4: Visualization 2 – Tip vs Total Bill (Scatter)
plt.figure(figsize=(8, 5))
sns.scatterplot(x="total_bill", y="tip", hue="time", data=df)
plt.title("Tip vs Total Bill by Time")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.savefig("tip_vs_bill.png", dpi=300)
plt.close()
print("📊 Saved: tip_vs_bill.png")

# Step 5: Visualization 3 – Tip Distribution by Gender (Boxplot FIXED)
if "sex" in df.columns and df["sex"].notna().any():
    df_clean = df.dropna(subset=["sex", "tip"])
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="sex", y="tip", data=df_clean)
    plt.title("Tip Distribution by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Tip ($)")
    plt.tight_layout()
    plt.savefig("tip_by_gender.png", dpi=300)
    plt.close()
    print("📊 Saved: tip_by_gender.png")
else:
    print("⚠️ Skipped boxplot: 'sex' column missing or empty.")

print("\n✅ All charts saved successfully.")

