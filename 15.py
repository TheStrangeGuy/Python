# Write a program to find out Fibonacci series using recursion and function as an object.

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fib(i))
