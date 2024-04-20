import numpy as np

# Filtering ith boolean index

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Return [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(f"Array {np1}")

# Only True can show numbers
# Normal Python
x = [True, True, False, False, True, False, True, True, False, False, True,  False]
print(f"Filtering with boolean manual array {np1[x]}")

# even numbers
# Normal Python
filtered = []
for y in np1:
    if y % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print(f"Filtering with boolean auto array {np1[filtered]}")

filter_np1 = np1 % 2 == 0
print(f"boolean auto array shortcut {filter_np1}")
print(f"Filtering with boolean auto array shortcut {np1[filter_np1]}")
