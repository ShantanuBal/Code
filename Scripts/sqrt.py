n = 100
def sqrt():
	global n
	i = 0
	j = n
	mid = (i+j)/2.0
	while abs((mid*mid)-n) > .001:
		if mid*mid > n:
			j = mid
		else:
			i = mid
		mid = (i+j)/ 2.0
	print mid

sqrt()
