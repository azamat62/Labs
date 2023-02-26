import re

a = input()
if re.search('a.*?b$', a):
    print('Found a match!')
else:
    print('Not matched!')