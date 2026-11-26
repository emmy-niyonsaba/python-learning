# Q3: Supermarket Product Price Determination
import numpy as np
from scipy.linalg import solve

# a) Equations (n = notebook, p = pen, c = pencil)
#   2n + 3p + 1c = 2900
#   3n + 2p + 2c = 3400
#   1n + 4p + 3c = 3100

# b) Coefficient matrix and totals
A = np.array([[2, 3, 1],
              [3, 2, 2],
              [1, 4, 3]])
b = np.array([2900, 3400, 3100])

# c) Solve
n, p, c = solve(A, b)
print(f"Notebook price = {n:.2f} RWF")
print(f"Pen price      = {p:.2f} RWF")
print(f"Pencil price   = {c:.2f} RWF")

# d) Verification by substitution
for name, row, total in zip("ABC", A, b):
    calc = row[0]*n + row[1]*p + row[2]*c
    print(f"Customer {name}: {row[0]}*{n:.0f} + {row[1]}*{p:.0f} + {row[2]}*{c:.0f} = {calc:.2f} (expected {total})  ->",
          "OK" if np.isclose(calc, total) else "MISMATCH")
print("All equations satisfied:", np.allclose(A @ np.array([n, p, c]), b))
