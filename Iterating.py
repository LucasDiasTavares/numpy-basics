import numpy as np

# Iterating

# 1D Array
# np1 = np.array([1, 2, 3, 4, 5, 6])

# Normal Python
# for x in np1:
#     print(x)

# 2D Array
# np2 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

# # Normal Python
# for x in np2:
#     for y in x:
#         print(y)

# 3D Array
np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Normal Python, here starts to complicated and slow app
# Return
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
for x in np3:
    for y in x:
        for z in y:
            print(f"Normal Python {z}")

# With Numpy
# Return
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
for x in np.nditer(np3):
    print(f"Numpy {x}")




