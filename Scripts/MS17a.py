# rotate 1D matrix

# These are global variables.
a = [1,2,3,4,5,6,7,8,9,10,11]
k = 3

def rotate():
	print a

	for i in range(k/2):
		flag = a[i]
		a[i] = a[k-i-1]
		a[k-i-1] = flag

	for i in range((len(a)-k)/2):
		flag = a[k+i]
		a[k+i] = a[len(a)-1-i]
		a[len(a)-1-i] = flag
	
	for i in range(len(a)/2):
		flag = a[i]
		a[i] = a[len(a)-1-i]
		a[len(a)-1-i] = flag

	print a

rotate()
