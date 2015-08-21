m = [40,20,30,10,30]
#m = [10,30,5,60]

def find(m):
	print m
	mul = 0
	print mul
	while len(m) > 2:
		min_val = 1000000
		for i in range(1,len(m)-1):
			if m[i-1]*m[i]*m[i+1] < min_val:
				min_index = i; min_val = m[i-1]*m[i]*m[i+1]
		m.pop(min_index)
		mul += min_val
		print m
		print mul
		print min_index

find(m)
