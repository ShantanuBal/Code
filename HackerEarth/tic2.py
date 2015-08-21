import time
start = time.time()


def input():
	m = []
	for i in range(3):
		m.append([int(each) for each in raw_input().split(' ')])
	p = int(raw_input())
	return m,p

def place(i,a,p,o,condition):
	if array[i][0] == p:
		if array[i][1] == p:
			print "XXX"
		else:
			print "XXX"
	else:
		print "XXX"


m,p = input()
if p==2:
	o = 1
else:
	o = 2
 
array = [
	m[0],m[1],m[2],
	[[m[0][0]]+[m[1][0]]+[m[2][0]]],
	[[m[0][1]]+[m[1][1]]+[m[2][1]]],
	[[m[0][2]]+[m[1][2]]+[m[2][2]]],
	[[m[0][0]]+[m[1][1]]+[m[2][2]]],
	[[m[0][2]]+[m[1][1]]+[m[2][0]]]
	]

for i in range(len(array)):
	if array[i].count(p) == 2 and array[i].count(0) == 1:
		place(i,array[i],p,o,1)
	elif array[i].count(o) == 2 and array[i].count(0) == 1:
		place(i,array[i],p,o,2)
		

print time.time() - start
