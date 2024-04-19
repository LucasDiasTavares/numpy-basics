import numpy as np

# Sorting

# Numbers
np1 = np.array([1, 5, 6, 4, 2, 3])
print(f"Array NP1 {np1}")
# Return [1 2 3 4 5 6]
print(f"NP1 sorting {np.sort(np1)}")

# String
np2 = np.array(['Lucas', 'Dias', 'Tavares', 'Milton', 'Pedro', 'Adriana', 'Santos'])
print(f"Array NP2 {np2}")
# Return ['Adriana' 'Dias' 'Lucas' 'Milton' 'Pedro' 'Santos' 'Tavares']
print(f"NP2 sorting {np.sort(np2)}")

# Bool
np3 = np.array([True, False, False, True, True, False, True])
print(f"Array NP3 {np3}")
# Return [False False False  True  True  True  True]
print(f"NP3 sorting {np.sort(np3)}")

# 2D Array
np4 = np.array([[1, 3, 2, 4, 7, 5, 6, 20], [8, 10, 12, 11, 14, 9, 13, 21]])
# Sort inside every individual item
print(f"Array NP4 {np4}")
# Return [[ 1  2  3  4  5  6  7] [ 8  9 10 11 12 13 14]]
print(f"NP4 sorting {np.sort(np4)}")
