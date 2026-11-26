# Q4: Agricultural Production Optimization
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# a) Production function
def production(x):
    return -2 * x**2 + 80 * x + 500

# b) Maximize by minimizing the negative of P(x), bounded to [0, 40]
res = minimize_scalar(lambda x: -production(x), bounds=(0, 40), method="bounded")
x_opt = res.x

# c) Maximum production
p_max = production(x_opt)
print(f"Optimal fertilizer : {x_opt:.2f} kg")
print(f"Maximum production : {p_max:.2f} units")
print("Check (analytic): x = -b/2a = 80/4 = 20 kg, P(20) = 1300")

# d) Plot
x = np.linspace(0, 40, 400)
plt.figure(figsize=(7, 5))
plt.plot(x, production(x), label="P(x) = -2x² + 80x + 500")
plt.scatter([x_opt], [p_max], color="red", zorder=5, label=f"Optimum ({x_opt:.1f} kg, {p_max:.0f})")
plt.axvline(x_opt, color="red", linestyle="--", alpha=0.5)
plt.title("Crop Production vs Fertilizer")
plt.xlabel("Fertilizer (kg)")
plt.ylabel("Production")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig("Q4_plot.png", dpi=150)
plt.show()
