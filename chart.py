# chart.py
# Author: 23f1001171@ds.study.iitm.ac.in
# Generates a professional Seaborn scatterplot for marketing effectiveness

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

# Campaign type (categorical variable for color differentiation)
campaign_type = np.random.choice(["Email", "Social Media", "TV Ads"], size=n, p=[0.3, 0.4, 0.3])

# Build DataFrame
df = pd.DataFrame({
    "Marketing_Spend": marketing_spend,
    "Customers_Acquired": customers_acquired,
    "Campaign_Type": campaign_type
})

# --- Visualization ---
sns.set_style("whitegrid")
sns.set_context("talk")  # professional presentation style

plt.figure(figsize=(8, 8))  # ensures 512x512 when saved with dpi=64

# Scatterplot
sns.scatterplot(
    data=df,
    x="Marketing_Spend",
    y="Customers_Acquired",
    hue="Campaign_Type",
    palette="Set2",
    s=80,
    edgecolor="black",
    alpha=0.8
)

# Titles and labels
plt.title("Marketing Spend vs Customer Acquisition", fontsize=16, weight="bold")
plt.xlabel("Marketing Spend ($1000s)", fontsize=14)
plt.ylabel("Customers Acquired", fontsize=14)
plt.legend(title="Campaign Type")

# Save chart as PNG (512x512)
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
