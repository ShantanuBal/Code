#rotated array

a = [9,3,4,5,6,7,8]

def find(l,r):
	if a[l] < a[r]:
		return a[l]
	if l == r-1 or l==r:
		return min(a[l],a[r])
	
	m = (l+r)/2
	if a[m] > a[l]:
		return find(m,r)
	else:
		return find(l,m)

print a
print find(0,len(a)-1)
