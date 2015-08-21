
a = [10,4,8,2,6,1,3,9,5,7]
print a

def quicksort(l,r):
	global a
	if l >= r:
		return
	if l == r-1:
		if a[l] > a[r]:
			flag = a[l]
			a[l] = a[r]
			a[r] = flag
		return

	pivot = a[l]
	i = l+1
	j = r
	while i<j:
		while a[i] < pivot and i<j:
			i += 1
		while a[j] > pivot and i<j:
			j -= 1
		if i<j:
			flag = a[i]; a[i] = a[j]; a[j] = flag
			i += 1; j -= 1
	if a[l] > a[j]:
		flag = a[l]; a[l] = a[j]; a[j] = flag
	print a
	quicksort(l,j-1)
	quicksort(i,r)
	

quicksort(0,len(a)-1)
print a
