# Jump Game

a = [3,1,4,1,0,0,1]

def find_opt():
	max = 0; i = 0
	while i<=max and i<len(a): 
		if a[i]+i > max:
			max = a[i] + i
		i += 1
	print a
	print max
	if max>=len(a)-1:
		print "YES"
	else:
		print "NO"
find_opt()
