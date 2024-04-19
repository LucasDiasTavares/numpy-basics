import numpy as np

# Searching - Return Index

# 1D Array
np1 = np.array([1, 2, 3, 4, 5, 6])
print(f"Array {np1}")

# Return (array([2], dtype=int64),)
# array type of data
# [2] means index 2
# int64 type of data
x = np.where(np1 == 3)

print(np.where(np1 == 3))

# Return [2] means index 2
print(x[0])

# 1D Array
np2 = np.array([1, 2, 3, 4, 5, 6, 3])
print(f"Array {np2}")
y = np.where(np2 == 3)

# Return [2 6] means index 2 and index 6
print(y[0])

# Searching - Return Value
print(f'Searching Value 3 inside NP1{np1[x[0]]}')
print(f'Searching Value 3 inside NP2 {np2[y[0]]}')

# Searching - if/else

z = np.where(np1 % 2 == 0)
# Return [1 3 5]
print(f'Even numbers {z[0]}')

