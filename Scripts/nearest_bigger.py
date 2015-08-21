a = [7, 5, 3, 2, 4, 1, 2, 9, 11 ]

def solve(a):
	b = [-1] * len(a)
	b[len(a)-1] = a[-1]
	for i in range(len(a)-2,0,-1):
		if a[i] < a[i+1]:
			b[i] = a[i+1]
	for each in a:
		print each,"\t",
	print
	for each in b:
		print each,"\t",
	print
	
solve(a)
