import time
start = time.time()
N = 4
number = []
x = 0
for i in range(N):
    number.append(x)
    if x == 109:
        x = 0
    else:
        x += 1
number = [0,1,3,2]

while True:
	print number
	i = 2
	while i<N:
		if number[i-2] == 0 and number[i-1] != 0 and number[i] == 0:
			print 'NO'; print time.time() - start; exit()
		i += 1
	count = number.count(0)
	if count == N:
		print 'YES'; break
	m = max(number)
	i = number.index(m)
	if i+1<N and number[i+1] != 0:
		if i-1 >= 0 and number[i-1]<number[i+1]:
			diff = number[i] - number[i-1]
			number[i] = number[i-1]; number[i+1] -= diff
		else:
			number[i] -= number[i+1]; number[i+1] = 0
	elif i-1>=0 and number[i-1] != 0:
		if i+1<N and number[i+1]<number[i-1]:
			number[i] = number[i+1]; number[i-1] = number[i+1]
		else:
			number[i] -= number[i-1]; number[i-1] = 0
	else:
		print 'NO'
		break
print time.time() - start
