# Perform Addition, Multiplication for Vectors and Matrices.

import numpy as np

# Addition of matrix
X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[10, 11, 12],
     [13, 14, 15],
     [16, 17, 18]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
print("Addition of matrix")
for r in result:
    print(r)

# Multiplication of matrix
Z = [[19, 20, 21, 22],
     [23, 24, 25, 26],
     [27, 28, 29, 30]]

res = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]


for i in range(len(X)):
    for j in range(len(Z[0])):
        for k in range(len(Z)):
            res[i][j] += X[i][k] * Z[k][j]

print("Multiplication of matrix")
for g in res:
    print(g)

# dot product in vector
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.dot(x, y)
print("dot product in vector")
print(z)

# cross product in vector
a = np.cross(x, y)
print("cross product in vector")
print(a)