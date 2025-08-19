# chart.py
# Author: 23f1001171@ds.study.iitm.ac.in
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

# Build DataFrame
df = pd.DataFrame({
    "Marketing_Spend": marketing_spend,
    "Customers_Acquired": customers_acquired,
    "Campaign_Type": campaign_type
})

# --- Visualization ---
sns.set_style("whitegrid")       # professional look
sns.set_context("talk")          # presentation-ready font sizes

plt.figure(figsize=(8, 8))       # ensures 512x512 pixels at dpi=64

# Boxplot: Customer acquisition by campaign type
sns.boxplot(
    data=df,
    x="Campaign_Type",
    y="Customers_Acquired",
    hue="Campaign_Type",          # assign hue same as x
    palette="Set2",               # professional color palette
    legend=False                  # avoid duplicate legend
)

# Titles and labels
plt.title("Customer Acquisition by Campaign Type", fontsize=16, weight="bold")
plt.xlabel("Campaign Type", fontsize=14)
plt.ylabel("Customers Acquired", fontsize=14)

# Save chart as PNG (exactly 512x512 pixels)
plt.savefig("chart.png", dpi=64)   # no bbox_inches="tight" → keeps exact 512x512
plt.close()
