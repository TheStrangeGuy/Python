# Practical based on Strings (Length finding, change specific character, palindrome, concatenation)

# Length finding
a = "TheStrangeGuy"
print(len(a))

# change specific character
x = a.replace("u", "x")
print(x)

# palindrome
# b = reversed(a)
if a == a[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# concatenation
y = "Astro"
z = a + " " + y
print(z)

