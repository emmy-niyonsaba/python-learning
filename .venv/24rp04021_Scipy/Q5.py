# Q5: Health Center Distance Analysis
import numpy as np

patient = np.array([4, 5])
health_centers = {"Center A": [8, 9], "Center B": [5, 7],
                  "Center C": [12, 4], "Center D": [3, 3]}

# a) + b) Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2), stored in a dictionary
distances = {name: float(np.sqrt(np.sum((np.array(c) - patient) ** 2)))
             for name, c in health_centers.items()}
print("Distances (km):")
for k, v in distances.items():
    print(f"  {k}: {v:.3f}")

# c) Sort by increasing distance
sorted_centers = sorted(distances.items(), key=lambda item: item[1])
print("\nSorted by distance:")
for k, v in sorted_centers:
    print(f"  {k}: {v:.3f} km")

# d) Nearest center
min_dist = sorted_centers[0][1]
# Handle ties: Center B and Center D are both exactly sqrt(5) km away
nearest = [k for k, v in sorted_centers if abs(v - min_dist) < 1e-9]
print(f"\nNearest center: {' and '.join(nearest)} at {min_dist:.3f} km (straight-line distance)")
if len(nearest) > 1:
    print("Note: there is a tie. Both are equally close; the final choice can use another criterion (e.g. road access, services).")
