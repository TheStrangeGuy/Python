# Write a python program to find out even numbers from a list using filter ().


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

ans = filter(lambda x: x % 2 == 0, list1)
print(list(ans))
