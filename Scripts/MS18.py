# missing numbers

a = [1,2,3,4,5,6,7,8,10]

def find_missing_number(a, l, r):
	print a[l:r+1]
	m = (l+r)/2
	if a[m] == a[m-1] + 2:
		return a[m-1] + 1
	if a[m] == a[m+1] - 2:
		return a[m+1] - 1
	elif a[m] == m+1:
		return find_missing_number(a, m+1, r)
	elif a[m] == m+2:
		return find_missing_number(a, l, m-1)
	
if a[-1] == len(a):
	print a[-1] + 1
elif a[0] != 1:
	print 1
else:
	print find_missing_number(a,0,len(a)-1)
