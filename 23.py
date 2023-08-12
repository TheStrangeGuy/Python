# A program to read a string from the user and append it into a file.

myfile = open("xyz.txt","a")
str = input("Enter a string to input in text file ")
myfile.write(str)
myfile.close()