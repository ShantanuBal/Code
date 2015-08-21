a = [20,30,10,11,12,13,15,16,17,18,19]
v = 17

def bin_search(a,e,l,r):
	if l>r:
		return False
	m = (l+r)/2

	if e < a[m]:
		return bin_search(a,e,l,m-1)
	if e > a[m]:
		return bin_search(a,e,m+1,r)
	return m+1

def bin_search_mod(a,e,l,r):
	if l>r:
		return False
	m = (l+r)/2

	if a[m] == e:
		return m+1
	if a[l] < a[m]:
		if a[l] <= e < a[m]:
			return bin_search(a,e,l,m-1)
		else:
			return bin_search_mod(a,e,m+1,r)

	else:
		if a[m] < e <= a[r]:
			return bin_search(a,e,m+1,r)
		else:
			return bin_search_mod(a,e,l,m-1)

print bin_search_mod(a,v,0,len(a)-1)
