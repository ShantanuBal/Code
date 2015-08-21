# Jump Game

a = [3,1,2,1,0,0,1]
b = [0] * len(a)
b[0] = 1
max = 0

def find_opt():
	global max
	i = 0
	while b[i] == 1 and i<len(a):
		if a[i]+i >= len(a)-1:
			print "Yes"
			print a
			print b
			return
		if a[i]+i > max:
			for j in range(max+1,1+a[i]+i):
				b[j] = 1
			max = a[i] + i
		i += 1
	print "No"
	print a
	print b

find_opt()
