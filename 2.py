
# Demonstrate arrays (Insertion, Deletion, arithmetic operations).
import numpy as np

arr = [10, 20, 30, 40, 50]

print(arr)

# insertion
arr.insert(1, 60)
print(arr)

# deletion
arr.remove(40)
print(arr)

# AO
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
add = np.add(arr1, arr2)

print("Addition: ", add)

