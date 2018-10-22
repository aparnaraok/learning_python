import re
greet = 'hello my\nworld'
pat1 = re.compile('hello$', re.MULTILINE) #Checks every line and matches the string ending with hello
print(pat1.search(greet))

pat2 = re.compile('.+', re.DOTALL)
print(pat2.search(greet))