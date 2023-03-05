items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('lab6\dir\items.txt','w')
for item in items:
    file.write(item+"\n")
file.close()