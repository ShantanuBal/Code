a = [7,6,5,4,3,2,1]

def merge(l,m,r):
	global a
	i,j = l,m
	flag = []
	while i <= m-1 and j <= r:
		if a[i] < a[j]:
			flag.append(a[i])
			i += 1
		else:
			flag.append(a[j])
			j += 1
	if i > m-1:
		while j <= r:
			flag.append(a[j])
			j += 1
	else:
		while i<= m-1:
			flag.append(a[i])
			i += 1
	
	a[l:r+1] = flag
	print a

def mergesort(l,r):
	global a
	m = (l+r+1)/2
	if l == r:
		return
	
	mergesort(l,m-1)
	mergesort(m,r)
	merge(l,m,r)


print a
mergesort(0,len(a)-1)
