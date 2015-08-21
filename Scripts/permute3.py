# Permutations

a = ['a','b','c','d']

def swap(i,j):
	flag = a[i]; a[i] = a[j]; a[j] = flag

def permute(l,r):
	if l>=r:
		print a; return
	
	for i in range(l,r+1):
		swap(i,l)
		permute(l+1,r)
		swap(i,l)

permute(0,len(a)-1)
