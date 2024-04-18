import numpy as np

# Slicing Numpy Arrays

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Return [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(f"Array {np1}")

# Return [2 3 4 5]
print(f"Simple Slice {np1[1:5]}")

# Return [ 4  5  6  7  8  9 10 11 12]
print(f"Simple Slice start index 3 {np1[3:]}")

# Return Negative [10 11]
print(f"Simple Slice with negative index {np1[-3:-1]}")

# Steps

# Return [2 3 4 5]
print(f"Simple Step {np1[1:5]}")

# Return [2 4] steps of 2
print(f"Simple Step of 2 {np1[1:5:2]}")

# Return [ 1  3  5  7  9 11] every other item
print(f"Simple every other item {np1[::2]}")

# Slice 2D array
np2 = np.array([
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12]
])

# Pull out a single item
# Index 1 meaning second item
# Second index 2 meaning third item
# Return 9
print(f"2D array - pull out a single item {np2[1,2]}")

# Pull out number from given position
# Return [[2 3]]
print(f"2D array - pull out a number from given position {np2[0:1, 1:3]}")

# Slice from both rows
# Return [[2 3] [8 9]]
print(f"2D array - slice from both rows {np2[0:2, 1:3]}")


