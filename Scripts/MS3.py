# Rotate a matrix
a = 	[	
	[11,12,13,14,15],
	[21,22,23,24,25],
	[31,32,33,34,35],
	[41,42,43,44,45],
	[51,52,53,54,55]
	]


def rotate(a):
	for each in a:
		print each

	for i in range(len(a)/2):
		print "\n",i,": ",
		for j in range(i,len(a)-1-i):
			print j,
			flag = a[i][j]
			a[i][j] = a[j][len(a)-1-i]
			a[j][len(a)-1-i] = a[len(a)-1-i][len(a)-1-j]
			a[len(a)-1-i][len(a)-1-j] = a[len(a)-1-j][i]
			a[len(a)-1-j][i] = flag
	print
	for each in a:
		print each


rotate(a)	
