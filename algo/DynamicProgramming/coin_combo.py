n = 4
c = [1,2,3]
def find(n,c):
	opt = [0] * (n+1)
	opt[0] = 1
	for i in range(len(c)):
		for j in range(c[i],n+1):
			opt[j] += opt[j-c[i]]
	print opt

find(n,c)
