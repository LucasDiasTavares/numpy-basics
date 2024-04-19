import numpy as np

# Shape and Reshape

np1 = np.array([1, 2, 3, 4, 5, 6])
print(f"Array {np1}")

# 1D and get shape

# Return (6,) 6 elements inside array
print(f"NP1 shape {np1.shape}")

# 2D and get shape (rows and columns)
np2 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

# Return (2, 6) 2 arrays and 6 elements inside
# If 2D with random quantity inside each array:
# ValueError: setting an array element with a sequence.
# The requested array has an inhomogeneous shape after 1 dimensions.
# The detected shape was (2,) + inhomogeneous part.
print(f"NP2 shape {np2.shape}")

# Reshape 2D

np3 = np1.reshape(2, 3)
# Return [[1 2 3] [4 5 6]]
print(f"NP3 {np3}")
# Return (2, 3)
print(f"NP3 shape {np3.shape}")

# Reshape 3D
np4 = np1.reshape(3, 2)
# Return [[1 2] [3 4] [5 6]]
print(f"NP4 {np4}")
# Return (2, 3)
print(f"NP4 shape {np4.shape}")

# Flat to 1D
np5 = np4.reshape(-1)
print(f"NP5 flat array {np5}")
# Return (6,) like np1.shape
print(f"NP5 flat array shape {np5.shape}")

# Any D to 1D
