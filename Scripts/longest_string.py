a = "ghelloworldx"
b = "zeslogrd"

def find(a,b):
	a = "0" + a
	b = "0" + b
	opt = []
	for each in range(len(b)): opt.append([0]*len(a))
	
	for i in range(1,len(b)):
		for j in range(1,len(a)):
			if b[i] == a[j]:
				opt[i][j] = 1 + opt[i-1][j-1]
			else:
				opt[i][j] = max(opt[i-1][j],opt[i][j-1])
	print
	print " ",
	for i in range(len(a)):
		print a[i],
	print
	for i in range(len(b)):
		print b[i],
		for j in range(len(a)):
			print opt[i][j],
		print
	text = ""
	i, j = len(b) - 1, len(a) - 1
	while i>=0 and j>= 0:
		if opt[i][j] == opt[i][j-1]:
			j -= 1
		elif opt[i][j] == opt[i-1][j]:
			i -= 1
		else:
			text += a[j]
			i -= 1; j -= 1
		
	print text[::-1]

find(a,b)
