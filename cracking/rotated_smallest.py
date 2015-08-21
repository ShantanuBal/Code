
def smallest(a, l, r):
	if l == r-1:
		return min(a[l],a[r])
	m = (l + r) / 2
	if a[m-1] > a[m]:
		return a[m]
	if a[l] < a[m]:
		print a[m:r+1]
		return smallest(a, m, r)
	#if a[m] < a[r]:
	else:
		print a[l:m+1]
		return smallest(a, l, m)

a = [5,6,7,8,9,2]

if a[0] < a[len(a)-1]:
	print a[0]
else:
	print smallest(a, 0, len(a)-1)
