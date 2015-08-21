# largest continious sum

a = [-2, -3, 4, -1, -2, 1, 5, -3]

def find():
	
	largest = -1; sum = 0
	for i in range(len(a)):
		if sum + a[i] < 0:
			x = i+2
			sum = 0
		else:
			sum += a[i]
		if sum > largest:
			y = i+1
			largest = sum
	print a
	print x, y
	return largest

print find()
