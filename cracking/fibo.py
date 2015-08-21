
limit = 15

def fibo(count, limit, x, y):
	print count, "\t", y
	if count == limit:
		return y
	return fibo(count+1, limit, y, x+y)

print fibo(2, limit, 0, 1)
