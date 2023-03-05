with open('lab6\dir\irst.txt','r') as firstfile, open('lab6\dir\second.txt','a') as secondfile:
    for line in firstfile:
             secondfile.write(line)