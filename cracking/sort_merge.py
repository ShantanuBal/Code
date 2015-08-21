
a = [10,9,8,7,6,5,4,3,2,1]

def merge(l, m, r):
	global a
	x = a[l:m+1]
	y = a[m+1:r+1]
	i = l

	while x and y:
		if x[0] < y[0]:
			a[i] = x.pop(0)
		else:
			a[i] = y.pop(0)
		i += 1
	while x:
		a[i] = x.pop(0)
		i += 1
	while y:
		a[i] = y.pop(0)
		i += 1
	print a

def merge_sort(l, r):
	global a
	if l >= r:
		return
	m = (l+r)/2
	merge_sort(l, m)
	merge_sort(m+1, r)
	merge(l, m, r)

print a
merge_sort(0, len(a)-1)
