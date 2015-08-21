
a = [20, 10, 30, 0, 100, 40, 30, 20, 0, 20, 30, 40, 50, 60, 50, 60, 70]

def find_local_min(a):
	max = -1
	start = a[0]
	for i in range(1,len(a)):
		if a[i] < start:
			start = a[i]
		if a[i] - start > max:
			max = a[i] - start
	print max

find_local_min(a)
