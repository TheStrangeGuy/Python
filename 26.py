# A program to append the contents of one file to another file.

# opening both files in read only mode to read initial contents
f1 = open("xyz.txt", 'r')
f2 = open("copied_file.txt", 'r')

# printing the contents of the file before appending
print('content of first file before appending -', f1.read())
print('content of second file before appending -', f2.read())

# closing the files
f1.close()
f2.close()

# opening first file in append mode and second file in read mode
f1 = open("xyz.txt", 'a+')
f2 = open("copied_file.txt", 'r')

# appending the contents of the second file to the first file
f1.write(f2.read())

# relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

# printing the contents of the files after appendng
print('content of first file after appending -', f1.read())
print('content of second file after appending -', f2.read())

# closing the files
f1.close()
f2.close()
