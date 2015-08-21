

def quicksort(a, l, r):
	if r<=l:
		return a
	else:
		org_l = l; org_r = r
		pivot = (l + r) / 2
		while l < r:
			while a[l] < a[pivot]:
				l += 1
			while a[r] > a[pivot]:
				r -= 1
			if l<r:
				flag = a[l]
				a[l] = a[r]
				a[r] = flag
				l += 1
				r -= 1
		a = quicksort(a, org_l, pivot-1)
		a = quicksort(a, pivot+1, org_r)
		return a

print quicksort([10,9,8,7,6,5,4,3,2,1],0,9)
