# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")

rev_fname = fname[::-1]
rev_lname = lname[::-1]

print(rev_lname + " " + rev_fname)


