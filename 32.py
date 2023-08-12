# Write a Python program to print out a set containing all the colours from color_list_1 which are not present in color_list_2.


a = {"Blue", "Yellow", "Black"}

b = {"Yellow", "Red", "White"}

print(a.difference(b))

print(b.difference(a))
