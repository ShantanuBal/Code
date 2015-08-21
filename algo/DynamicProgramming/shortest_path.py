a = [[1,2,3],[4,8,2],[1,5,3]]
opt = a

def find(a,opt):
	for i in range(1,3):
		opt[i][0] += opt[i-1][0] 
		opt[0][i] += opt[0][i-1]

	for i in range(1,3):
		for j in range(1,3):
			opt[i][j] += min(opt[i-1][j-1], opt[i-1][j], opt[i][j-1])

	for each in opt:
		print each

find(a,opt)

