import re

a = input()
if re.match(r"ab{2,3}$", a):
    print(True)
else:
    print(False)