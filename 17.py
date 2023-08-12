# Write a Python program to check whether a specified value is contained in a group of values using lambda function.
# Test Data:
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


lam = lambda x, n: True if n in x else False

print(lam([1, 5, 8, 3], 3))
print(lam([5, 8, 3], -1))

