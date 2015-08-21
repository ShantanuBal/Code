

a = [
	[1,1,1,1,1],
	[2,2,2,2,2],
	[3,3,3,3,3],
	[4,4,4,4,4],
	[5,5,5,5,5]
    ]

for each_row in a:
	for each_element in each_row:
		print each_element, " ",
	print
print

def rotate(a):
	size = len(a) - 1
	for i in range(len(a)/2):
		for j in range(i, size - i)[::-1]:
			"""
			flag = a[i][j]
			a[i][j] = a[j][size-i]
			a[j][size-i] = a[size-i][size-j]
			a[size-i][size-j] = a[size-j][i]
			a[size-j][i] = flag
			"""
			flag = a[i][j]
			a[i][j] = a[size-j][i] 
			a[size-j][i] = a[size-i][size-j] 
			a[size-i][size-j] = a[j][size-i] 
			a[j][size-i] = flag

	return a


a = rotate(a)
for each_row in a:
	for each_element in each_row:
		print each_element," ",
	print
