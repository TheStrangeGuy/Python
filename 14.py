# Write a function to find out the factorial of a given number. I) without recursion II) with recursion

# (a) without Recursion
n = int(input("Enter a number:"))
x = 1
while n > 0:
    x = x * n
    n = n - 1
print("Factorial of the number is: ")
print(x)


# (b) with recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = int(input("Enter a number: "))
if num < 0:
    print("no factorial for negative numbers")
elif num == 0:
    print("factorial is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
