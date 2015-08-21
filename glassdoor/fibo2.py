def fibo(n, a):
	if len(a) < n:
		fibo(n, a + [a[-1]+a[-2]])
	else:
		print a

fibo(10,[0,1])
