
a = [[1,2,3,4],[6,7,8,9],[11,12,13,14],[16,17,18,19]]

def rotate(a):

	for each in a:
		print each
	print

	for i in range(len(a)/2):
		for j in range(i,len(a)-1-i):
			flag = a[i][j]

			a[i][j] = a[j][len(a)-1-i]

			a[j][len(a)-1-i] = a[len(a)-1-i][len(a)-1-j]

			a[len(a)-1-i][len(a)-1-j] = a[len(a)-1-j][i]

			a[len(a)-1-j][i] = flag

	for each in a:
		print each
	print

rotate(a)
