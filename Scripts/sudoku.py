# sudoku

a = [[1,0,0],[0,0,0],[0,0,0]]
stack = []

def add(i, j, k):
	row, col = [], []
	for p in range(len(a)):
		row.append(a[i][p]) 
		col.append(a[p][j])

	for value in range(k,len(a)+1):
		if value not in row and value not in col:
			return value
	return -1

def fill():
	i = 0
	while i<len(a):
		j = 0
		while j<len(a):
			if a[i][j] == 0:
				top = [i,j,1]
				val = add(i,j,a[i][j]+1)
				while( val == -1 ):
					top = stack.pop()
					val = add(top[0], top[1], top[2]+1)
				i, j = top[0], top[1]
				a[i][j] = val
				stack.append([i,j,val])
			j += 1
		i += 1

for each in a:
	print each
fill()
print
for each in a:
	print each
