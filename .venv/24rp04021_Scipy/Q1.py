# Q1: Student Performance Statistical Analysis (SciPy)
import numpy as np
from scipy import stats

marks = np.array([45, 67, 78, 89, 56, 90, 72, 67, 84, 95, 58, 76, 81, 67, 93])

# a) Mean, variance, skewness, kurtosis
mean = np.mean(marks)
variance = np.var(marks, ddof=1)          # sample variance
skewness = stats.skew(marks)
kurt = stats.kurtosis(marks)              # excess (Fisher) kurtosis
print(f"Mean     : {mean:.2f}")
print(f"Variance : {variance:.2f} (sample, ddof=1)")
print(f"Skewness : {skewness:.4f}")
print(f"Kurtosis : {kurt:.4f} (excess)")

# b) Mode
mode_res = stats.mode(marks, keepdims=False)
print(f"Mode     : {mode_res.mode} (appears {mode_res.count} times)")

# c) Standard deviation
std = np.std(marks, ddof=1)
print(f"Std Dev  : {std:.2f} (sample)")

# d) Interpretation
print("\nInterpretation:")
print(f"- Median = {np.median(marks)}, mean = {mean:.2f}: close together, so the centre is stable.")
print(f"- Skewness = {skewness:.2f}: " + ("slightly negative -> a longer tail of low marks; most students scored high."
      if skewness < -0.1 else "approximately symmetric." if abs(skewness) <= 0.1 else "positively skewed."))
print(f"- Kurtosis = {kurt:.2f} (<0): flatter than a normal curve, marks are spread widely with no sharp peak.")
print(f"- Std dev = {std:.2f}: marks typically deviate about {std:.0f} points from the mean (range 45-95).")
print("- The mode (67) is below the mean, showing many average performers alongside a group of high achievers.")
