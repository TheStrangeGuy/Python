# A program to read the contents of a file in reverse order.

myfile = open("xyz.txt", "r")
for line in reversed(list(open("xyz.txt"))):
    print(line.rstrip())