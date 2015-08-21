# permutations of a set

a = ["a","b","c","d"]
count = 1

def swap(i,j):
	global a
	flag = a[i]
	a[i] = a[j]
	a[j] = flag

def permute(l,r):
	global a, count
	if l >= r:
		print count, ":", a
		count += 1
		return
	
	for k in range(l,r+1):
		swap(l,k)
		permute(l+1,r)
		swap(l,k)

permute(0,len(a)-1)
