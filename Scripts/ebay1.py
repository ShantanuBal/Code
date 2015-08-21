
a = [0, 10, 20, 10, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 50, 60, 70]

def find_local_min(a):
	for i in range(1,len(a)-1):
		if a[i-1] > a[i] and a[i+1] > a[i]:
			print a[i]

find_local_min(a)
