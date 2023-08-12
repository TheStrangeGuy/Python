myfile = open("xyz.txt", "r")


# to count the number of words
#
# data = myfile.read()
# words = data.split()
# print("The number of words in the text file is: ", len(words))

# to count the number of lines
#
# Counter = 0
# data = myfile.read()
# list = data.split("\n")
#
# for i in list:
#     if i:
#         Counter += 1
#
# print("Total number of lines in the text file is: ", Counter)
# lines = len(myfile.readlines())
# print("Total number of lines in the text file is: ", lines)

# # to count the occurence of a particular word

# data = myfile.read()
# occurences = data.count("Computer")
# print("The occurence of the word is: ", occurences)

# # occurence of a particular character

# count = 0
# char = input("ENTER CHARACTER : ")
# for i in myfile:
#     for c in i:
#         if c == char:
#             count = count + 1
# print("THE CHARACTER {} IS FOUND {} TIMES IN THE TEXT FILE".format(char, count))

# to count the number of blank spaces
#
# count = 0
# while True:
#     char = myfile.read(1)
#
#     if char.isspace():
#         count += 1
#     if not char:
#         break
#
# print("The number of blank spaces ", count)

myfile.close()



# print("this is been printed using readline")
# str = myfile.readline(10)
# print(str)
# print('\n')
#
# print("this is been printed using read")
# str1 = myfile.read(20)
# print(str1)
