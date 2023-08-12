# Write a python program to find out if a given number is even or odd using a user defined function.

def number(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


x = int(input("Enter a number"))
number(x)
