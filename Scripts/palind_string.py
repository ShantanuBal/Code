word = "XABACYUSABAL"

def find():
	global word
	a = [each for each in word]
	b = a[::-1]
	a.insert(0,'0')
	b.insert(0,'0')
	print "a:", a
	print "b:", b
	opt = []
	for i in range(len(word)+1):
		opt.append( [0] * (len(word)+1) )
	for i in range(1,len(word)+1):
		for j in range(1,len(word)+1):
			if a[i] == b[j]:
				opt[i][j] = 1 + opt[i-1][j-1]
			else:
				opt[i][j] = opt[i-1][j]
	
	for each in opt:
		print each
	
	i, j = len(word), len(word)
	while opt[i][j] != 0:
		if opt[i][j] == opt[i-1][j-1] + 1:
			print a[j]
			i -= 1; j -= 1
		else:
			j -= 1

find()
