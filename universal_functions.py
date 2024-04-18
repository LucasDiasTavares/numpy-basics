import numpy as np

# Universal Functions

np_positive = np.array([0, 1, 2, 3, 4, 5, 6])
np_positive_and_negative = np.array([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])

print(f"Array {np_positive}")

# Square of each element
print(f"Square of each element {np.sqrt(np_positive)}")

# Absolute Value
# change [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6] to [6 5 4 3 2 1 0 1 2 3 4 5 6]
print(f"Absolute Value {np.absolute(np_positive_and_negative)}")

# Exponential
print(f"Exponential {np.exp(np_positive_and_negative)}")

# Min or Max

# Return 6
print(f"Max value {np.max(np_positive_and_negative)}")

# Return -6
print(f"Min value {np.min(np_positive_and_negative)}")

# Sign positive or negative
# Return -1 if negative, 0 if zero and 1 if positive
print(f"Positive or negative {np.sign(np_positive_and_negative)}")
