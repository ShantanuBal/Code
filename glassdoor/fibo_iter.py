x = 0; y = 1
print x,"\n",y
for i in range(10):
	print x+y
	x = x + y
	y = x - y
	x = x - y
	y += x

