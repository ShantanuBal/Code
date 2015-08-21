x, p, q = 'abc', 0, 2

def swap(i, j):
	global x
	word = x[:i]
	word += x[j]
	word += x[i+1:j]
	word += x[i]
	word += x[j+1:]
	x = word

def permute(i, j):
	global x
	if i==j:
		print x
	else:
		for k in range(i,j+1):
			swap(i,k); permute(i+1,j); swap(i,k)

permute(p,q)
