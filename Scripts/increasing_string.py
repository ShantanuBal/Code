word = "XABACYUZABAL"

def find():
	global word
	a = [each for each in word]
	opt = [0] * (len(word))
	#for i in range(len(word)+1):
	#	opt.append( [0] * (len(word)+1) )
	for i in range(1,len(word)):
		max = 0
		for j in range(1,i):
			if a[i] > a[j]:
				if opt[j] + 1 > max:
					max = opt[j] + 1
			opt[i] = max
	for each in a:
		print each,
	print
	for each in opt:
		print each,
	print
	"""
	i, j = len(word), len(word)
	while opt[i][j] != 0:
		if opt[i][j] == opt[i-1][j-1] + 1:
			print a[j]
			i -= 1; j -= 1
		else:
			j -= 1
	"""
find()
