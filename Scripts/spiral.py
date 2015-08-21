#spiral printing

a = [[1,2,3,4],[6,7,8,9],[11,12,13,14],[16,17,18,19]]


def print_spiral():
	for each in a:
		print each
	print
	for i in range(1+ (len(a)/2)):
		print
		for j in range(i,len(a)-i-1):
			print a[i][j],
		for j in range(i,len(a)-i-1):
			print a[j][len(a)-i-1],
		for j in range(i,len(a)-i-1):
			print a[len(a)-1-i][len(a)-1-j],
		for j in range(i,len(a)-i-1):
			print a[len(a)-1-j][i],
	if len(a)%2:
		print a[i][i]

print_spiral()
