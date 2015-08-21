min = 10000

def opt():
	for i in range(0, 20/10 + 1):
		cash = 20 - 10*i
		for j in range(0, cash/5 + 1):
			cash -= 5*j
			for k in range(0, cash/3 + 1):
				l = 20 - i*10 - j*5 - k*3
				print i, j, k, l

print "d n 3 p"
opt()
print min
