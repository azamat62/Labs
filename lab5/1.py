import re

a = input()
if re.search(r"^a(b)*$", a):
    print(True)
else:
    print(False)