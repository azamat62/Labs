import re

a = input()
if re.search(r'^[a-z]+_[a-z]+$', a):
   print('Found a match!')
else:
   print('Not matched!')