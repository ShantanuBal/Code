a = ['a', 'b', 'c']

def swap(a, x, y):
	flag = a[x]; a[x] = a[y]; a[y] = flag
	return a

def permute(l, r):
	global a
	if l >= r:
		print a
		return
	for i in range(l, r+1):
		a = swap(a, i, l)
		permute(l+1, r)
		a = swap(a, i, l)
	
permute(0, len(a)-1)
