import re
a = input()
print(re.sub('(?<!^)(?=[A-Z])', ' ', a))