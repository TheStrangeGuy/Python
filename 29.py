# Write a Python program which accepts a sequence of comma-separated numbers from the user and generate a list and a tuple with those numbers.

csm = input("Enter values with comma (,) :")
list = csm.split(",")
tuple = tuple(list)

print(list)
print(tuple)
