import time
start = time.time()
n = [1,2,4,4,1]
N = len(n)
"""
for i in range(N):
    n.append(x)
    if x == 109:
        x = 0
    else:
"""
while True:
	print n
	if (n[0] != 0 and n[1] == 0) or (n[N-2] == 0 and n[N-1] != 0):
		print 'NO'; break
	i = 2
	while i<N:
		if n[i-2] == 0 and n[i-1] != 0 and n[i] == 0:
			print 'NO'; exit()
		i += 1

	counter = n.count(0)
	if counter == N:
		print "YES"; break

	m = max(n)
	i = n.index(m)
	if i>= 1 and n[i-1] != 0:
		n1 = n[i-1]
	else:
		n1 = 0
	if i<N-1 and n[i+1] != 0:
		n2 = n[i+1]
	else:
		n2 = 0
	print n1, n2
	if n1 and n2:
		if n1>n2:
			n[i] -= (n1-n2); n[i-1] = n2
		elif n1<n2:
			n[i] -= (n2-n1); n[i+1] = n1
		else:
			n[i] -= 2; n[i-1] -= 1; n[i+1] -= 1
	elif not n1 and n2:
		n[i] -= n2; n[i+1] = 0	
	elif n1 and not n2:
		n[i] -= n1; n[i-1] = 0
	else:
		print "NO"; break

print time.time() - start
