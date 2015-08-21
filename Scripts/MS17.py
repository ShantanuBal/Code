# rotate 1D matrix

# These are global variables.
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
k = 8

def rotate(s,k):
	global a
	for i in range(s,s+k):
		j = i
		while j+k < len(a):
			flag = a[j]
			a[j] = a[j+k]
			a[j+k] = flag
			j += k
	if k == 1:
		print a
	else:
		rotate(len(a)-k, k-((len(a)-s)%k) )

def main(): 
	global a,k
	print a
	rotate(0,k)

main()
