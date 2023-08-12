# A program to read a file and capitalize the first letter of every word in the file.

with open("xyz.txt", "rt") as file:
    file_txt = file.read()
print(file_txt.title())