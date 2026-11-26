# Q8: Customer Segmentation Using K-Means
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# a) DataFrame
df = pd.DataFrame({
    "Customer": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"],
    "Spending": [20000, 25000, 30000, 80000, 85000, 90000, 150000, 160000, 170000],
    "Visits":   [2, 3, 4, 10, 12, 11, 20, 22, 21]})
print(df, "\n")

# b) Standardize
X_scaled = StandardScaler().fit_transform(df[["Spending", "Visits"]])

# c) KMeans, 3 clusters
km = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = km.fit_predict(X_scaled)

# d) Add labels to ORIGINAL dataframe
df["Cluster"] = labels
print(df, "\n")

# e) Interpretation by cluster averages
summary = df.groupby("Cluster")[["Spending", "Visits"]].mean().round(1)
print(summary, "\n")
for cl, row in summary.sort_values("Spending").iterrows():
    level = "Low" if row.Spending < 50000 else "Medium" if row.Spending < 120000 else "High"
    print(f"Cluster {cl}: {level}-value customers (avg spending {row.Spending:,.0f} RWF, avg {row.Visits:.1f} visits/month)")
