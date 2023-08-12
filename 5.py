# Create a menu driven program to show various operators supported by python.

print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

choice = input("Enter your choice:")

num1 = int(input("Enter 1st no."))
num2 = int(input("Enter 2nd no."))

if choice == "1":
    print(num1, "+", num2, "=", (num1 + num2))

elif choice == "2":
    print(num1, "-", num2, "=", (num1 - num2))

elif choice == "3":
    print(num1, "*", num2, "=", (num1 * num2))

elif choice == "4":
    print(num1, "/", num2, "=", (num1 / num2))

else:
    print("Invalid choice")


