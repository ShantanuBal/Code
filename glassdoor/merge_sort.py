
def merge(a,l,m,r):
	x,y = [],[]
	for i in range(l,m):
		x.append(a[i])
	for j in range(m,r+1):
		y.append(a[j])
	i, j = 0, 0
	while i < len(x) and j<len(y):
		if x[i] < y[j]:
			a[l] = x[i]
			i += 1
		else:
			a[l] = y[j]
			j += 1
		l += 1
	while i<len(x):
		a[l] = x[i]
		l += 1
		i += 1
	while j<len(y):
		a[l] = y[i]
		l += 1
		j += 1
	return a

def merge_sort(a,l,r):
	if r<=l:
		return a
	else:
		m = (l+r+1) / 2
		a = merge_sort(a,l,m-1)
		a = merge_sort(a,m,r)
		print l, m, r
		return merge(a,l,m,r)

print merge_sort([10,9,8,7,6,5,4,3,2,1],0,9)
