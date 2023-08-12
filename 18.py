# Write a Python program to find whether a given string begins/ends with a given character using Lambda.


start1 = lambda x: True if x.startswith('C') else False
print(start1('Critical'))

start2 = lambda x: True if x.startswith('C') else False
print(start2('Astounding'))

end1 = lambda x: True if x.endswith('C') else False
print(end1('Condescending'))

end2 = lambda x: True if x.endswith('C') else False
print(end2('Cinematic'))

# It is case sensitive
end3 = lambda x: True if x.endswith('c') else False
print(end3('Cinematic'))