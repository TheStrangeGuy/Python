# An interactive program where one module asks numbers from the user and the second module performs at least three arithmetic operations on them.

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:

    H = input("Enter 1,2,3 or 4 \n")

    if H in ("1", "2", "3", "4"):
        a = int(input("ENTER FIRST NUMBER \n"))
        b = int(input("ENTER SECOND NUMBER \n"))

        if H == "1":
            print("Output:")
            print(add(a, b))

        elif H == "2":
            print("Output:")
            print(sub(a, b))

        elif H == "3":
            print("Output:")
            print(multi(a, b))

        elif H == "4":
            print("Output:")
            print(div(a, b))
    else:
        print("Invalid")

    break
