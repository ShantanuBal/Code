a = [3,4,7,1,2,9,8]
n = len(a)

def main():
	a.sort() # n log(n)
	i, j = 0, n-1
	p, q = i+1, j-1
	count = 1
	while i < j-2:
		if a[i] + a[j] == a[p] + a[q]:
			print a[i], a[j], a[p], a[q]
			p += 1
			q -= 1
		elif a[i] + a[j] > a[p] + a[q]:
			p += 1
		else:
			q -= 1
		if p>=q:
			if count == 1:
				i += 1
				count = 2
			elif count == 2:
				i -= 1
				j -= 1
				count = 3
			elif count == 3:
				i += 1
				count = 1
			p, q = i+1, j-1


main()
