n = 100
opt = [0] * (n+1)
store = [0] * (n+1)
where = [0] * (n+1)
def find():
	global opt, n
	opt[2] = 1
	for i in range(3,n+1):
		for k in range(2,i):
			if opt[i] < opt[k] * (i-k):
				opt[i] = opt[k] * (i-k)
				store[i] = i-k
				where[i] = 1
			if opt[i] < k * (i-k):
				opt[i] = k * (i-k)
				store[i] = k
				where[i] = 2
			
	for i in range(len(opt)):
		print i, "\t\t", opt[i], "\t\t", store[i], "\t\t", where[i]

find()
