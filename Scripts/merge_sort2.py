# Merge sort

a = [9,8,7,6,5,4,3,2,1]

def merge(l,m,r):

	flag = []
	i, j = l,m+1
	while i<=m and j<=r:
		if a[i] < a[j]:
			flag.append(a[i]); i+=1; 
		else:
			flag.append(a[j]); j+=1;
	if i>m:
		while j<=r:
			flag.append(a[j]); j+=1;
	if j>r:
		while i<=m:
			flag.append(a[i]); i+=1;
	a[l:r+1] = flag[:]
	print a
	
def merge_sort(l,r):
	if l>=r:
		return
	
	m = (l+r)/2
	merge_sort(l,m)
	merge_sort(m+1,r)
	merge(l,m,r)

print a
merge_sort(0,len(a)-1)
