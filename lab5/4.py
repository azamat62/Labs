import re

a = input()
if re.search(r'[A-Z]+[a-z]+$', a):
    print('Found a match!')
else:
    print('Not matched!')