n = 20
opt = []
for i in range(n+1):
	opt.append(i)
opt[2] = 1
print "Opt array:", opt

def maxprod():
	global opt, n
	for i in range(3, n + 1):
		max_val = -1
		for k in range(1,i):
			max_val = max(max_val, k * (i-k), opt[k]*(i-k))
		print opt[i], " : ",
		opt[i] = max_val
		print opt[i]

maxprod()
