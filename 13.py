# Write a function to find out x^y. Function should find out the square of x in case of default argument passing.

def fun():
    print("Value is:", x ** y)


x = int(input("Enter the value of x :"))
y = int(input("Enter the value of y :"))
fun()


def dfun(x, y):
    print("Value is:", x ** y)

dfun(x, 2)
