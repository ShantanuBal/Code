# to find shantanu zxcantazxc
a = "shantanucan"
b = "zxcantaxc"

def find():
	a1 = [each for each in a]
	a2 = [each for each in b]
	a1 = [0] + a1
	a2 = [0] + a2
	opt = []
	for each in a2:
		row = []
		for each in a1:
			row.append(0)
		opt.append(row)

	for i in range(1,len(a2)):
		for j in range(1,len(a1)):
			if a1[j] == a2[i]:
				print i,j
				opt[i][j] = opt[i-1][j-1] + 1

	print "  ",
	for each in a1:
		print each,'',
	print 
	i = 0
	for each in opt:
		print a2[i], each
		i += 1

find()
