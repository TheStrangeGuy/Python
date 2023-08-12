# A program to read a text file and print all the numbers present in the text file.

myfile = open("xyz.txt", "r")
for line in myfile:
    words = line.split()
    for i in words:
        for letter in i:
            if(letter.isdigit()):
                print(letter)