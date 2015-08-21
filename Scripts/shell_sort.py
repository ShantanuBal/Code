# shell sort

a = [10,9,8,7,6,5,4,3,2,1]
count = 0

def sort(a):
	global count
	i = len(a)/2
	while i>0:
		j = 0
		while j+i<len(a):
			k = j+i
			while k - i >= 0:
				if a[k-i] <= a[k]:
					break
				flag = a[k]; a[k] = a[k-i]; a[k-i] = flag
				k -= i
			count += 1
			j += 1
		print a, i
		i = i/2

print a
sort(a)
