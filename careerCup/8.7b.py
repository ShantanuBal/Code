sum = 10

for i in range(0,(sum/25)+1):
	r1 = sum - 25*i
	for j in range(0,(r1/10)+1):
		r2 = r1 - 10*j
		for k in range(0, (r2/5)+1):
			r3 = r2 - 5*k
			for l in range(0, (r3)+1):
				r4 = r3 - 1*l
			else:
				print i, j, k, l
