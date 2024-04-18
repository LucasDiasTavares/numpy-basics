import numpy as np

# View and Copy

np1 = np.array([0, 1, 2, 3, 4, 5, 6])

# View
np1_view = np1.view()

print(f"Original np1 {np1}")
print(f"Original np1_view {np1_view}")

# Change index 0 to value 99
np1[0] = 99

# Both changes
# Return [99  1  2  3  4  5  6]
print(f"Changed np1 {np1}")
print(f"Original np1_view {np1_view}")

# Copy
np2 = np.array([0, 1, 2, 3, 4, 5, 6])
np2_copy = np2.copy()

print(f"Original np2 {np2}")
print(f"Original np2_copy {np2_copy}")

# Change index 0 to value 99
np2[0] = 88

# Only original changed, vice versa
print(f"Changed np2 {np2}")
print(f"Original np2_copy {np2_copy}")

