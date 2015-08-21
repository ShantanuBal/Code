a = ['a','b','a','b','a','a','b']

def swap(i, j):
	global a
	flag = a[i]; a[i] = a[j]; a[j] = flag

def sort():
	global a
	i = 0
	j = len(a) - 1
	while i<j:
		while a[i] == 'a':
			i += 1
		while a[j] == 'b':
			j -= 1
		if i<j:
			swap(i, j)
			i += 1
			j -= 1
print a
sort()
print a
