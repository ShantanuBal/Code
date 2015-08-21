#permute string

def swap(string, p, q):
	x = [each for each in string]
	flag = x[p]
	x[p] = x[q]
	x[q] = flag
	y = ""
	for each in x:
		y += each
	return y

def permute(string, i, j):
	if i==j:
		print string
	else:
		for k in range(i, j+1):
			string = swap(string,i,k)
			permute(string,i+1,j)
			string = swap(string,i,k)

permute("abc",0,2)
