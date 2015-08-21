def fibo(x,y,count):
	if count < 10:
		print x+y
		fibo(y, x+y, count+1)

print 0
print 1
fibo(0,1,3)
