# chart.py
# Author: 23f10011714@ds.study.iitm.ac.in
# Generates a professional Seaborn boxplot for marketing effectiveness

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Generate synthetic business data ---
np.random.seed(42)
n = 200

# Marketing spend in thousands ($10k - $100k)
marketing_spend = np.random.uniform(10, 100, n)

# Customer acquisition with diminishing returns + noise
customers_acquired = 30 * np.log(marketing_spend) + np.random.normal(0, 10, n)

# Campaign type (categorical variable for grouping)
campaign_type = np.random.choice(["Email", "Social Media", "TV Ads"], size=n, p=[0.3, 0.4, 0.3])

# Bin marketing spend into categories (low, medium, high)
spend_bins = pd.cut(
    marketing_spend,
    bins=[10, 40, 70, 100],
    labels=["Low Spend", "Medium Spend", "High Spend"]
)

# Build DataFrame
df = pd.DataFrame({
    "Marketing_Spend": marketing_spend,
    "Spend_Level": spend_bins,
    "Customers_Acquired": customers_acquired,
    "Campaign_Type": campaign_type
})

# --- Visualization ---
sns.set_style("whitegrid")       # professional look
sns.set_context("talk")          # presentation-ready font sizes

plt.figure(figsize=(8, 8))       # ensures 512x512 when saved with dpi=64

# Boxplot: Customer acquisition by spend level & campaign type
sns.boxplot(
    data=df,
    x="Spend_Level",             # spend level on x-axis
    y="Customers_Acquired",      # acquisition as metric
    hue="Campaign_Type",         # color-coded by campaign type
    palette="Set2"               # professional palette
)

# Titles and labels
plt.title("Customer Acquisition by Spend Level and Campaign Type", fontsize=16, weight="bold")
plt.xlabel("Marketing Spend Level", fontsize=14)
plt.ylabel("Customers Acquired", fontsize=14)
plt.legend(title="Campaign Type")

# Save chart as PNG (512x512)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
