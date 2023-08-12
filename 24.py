# A program to copy the contents of one file into another.

myfile = open("xyz.txt", "r")
myfile1 = open("copied_file.txt","w")

str = " "
while str:
    str = myfile.readline()
    myfile1.write(str)
myfile.close()
myfile1.close()
print("File copied successfully! ")
