# Q2: Study Hours and Examination Performance
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# a) NumPy arrays
hours = np.array([2, 3, 4, 5, 6, 7, 8, 9])
marks = np.array([45, 50, 60, 65, 75, 80, 90, 95])

# b) Pearson correlation
r, p = pearsonr(hours, marks)
print(f"Pearson r = {r:.4f}")
print(f"p-value   = {p:.3e}")

# c) Interpretation
print("\nInterpretation:")
print("- Direction: positive (more study hours -> higher marks).")
print(f"- Strength: r = {r:.3f}, a very strong linear relationship (|r| > 0.9).")
print(f"- p-value = {p:.2e} < 0.05: statistically significant; unlikely to be due to chance.")
print("- Correlation does not prove causation; n = 8 is also a small sample.")

# d) Scatter plot
plt.figure(figsize=(7, 5))
plt.scatter(hours, marks, color="blue", s=60)
plt.title(f"Study Hours vs Marks (r = {r:.3f})")
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.grid(True, alpha=0.3)
plt.savefig("Q2_scatter.png", dpi=150)
plt.show()
