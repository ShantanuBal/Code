import time
start = time.time()

f = open('list.txt','r+')
text = f.read()
f.close()

list = []
number = ''
for each in text:
    if each == '\n':
        list.append(int(number))
        number = ''
    else:
        number += each
print list

print time.time() - start
