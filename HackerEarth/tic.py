import time
start = time.time()

def place(p):
	for i in range(3):
		count_p,count_0 = 0,0
		for j in range(3):
			if m[i][j] == p:
				count_p += 1
			if m[i][j] == 0:
				count_0 += 1; pos_0 = [i,j]
			if count_p == 2 and count_0 == 1:
				print pos_0[0], pos_0[1]; exit()

	for j in range(3):
		count_p, count_0 = 0, 0
		for i in range(3):
			if m[i][j] == p:
				count_p += 1
			if m[i][j] == 0:
				count_0 += 1; pos_0 = [i,j]
			if count_p == 2 and count_0 == 1:
				print pos_0[0], pos_0[1]; exit()

	count_p, count_0 = 0, 0
	for i in range(3):
		if m[i][i] == p:
			count_p += 1
		if m[i][i] == 0:
			count_0 += 1; pos_0 = [i,i]
		if count_p == 2 and count_0 == 1:
			print pos_0[0], pos_0[1]; exit()

	count_p, count_0 = 0, 0
	for i in range(3):
		if m[i][2-i] == p:
			count_p += 1
		if m[i][2-i] == 0:
			count_0 += 1; pos_0 = [i,2-i]
		if count_p == 2 and count_0 == 1:
			print pos_0[0], pos_0[1]; exit()
	
def input():
	m = []
	for i in range(3):
		m.append([int(each) for each in raw_input().split(' ')])
	p = int(raw_input())
	return m,p

m,p = input()
if p==2:
	o = 1
else:
	o = 2

place(p)
place(o)
	
print time.time() - start
