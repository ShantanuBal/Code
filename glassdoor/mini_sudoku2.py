a = [
	[3,0,0,0],
	[4,0,0,0],
	[0,0,0,0],
	[0,0,0,0],
    ]
limit = 4
stack = []

def find_valid(i,j,low):
	global a, limit
	for k in range(low+1,limit+1):
		if k not in a[i] and k not in [a[0][j], a[1][j], a[2][j], a[3][j]]:
			return k
	else:
		return -1

def sudoku():
	global a, stack, limit
	i = 0
	while i<limit:
		j = 0
		while j<limit:
			if a[i][j] == 0:
				x = find_valid(i,j,0)
				if x == -1:
					[pos_i, pos_j, value] = stack.pop()
					a[pos_i][pos_j] = find_valid(pos_i,pos_j,value)
					while a[pos_i][pos_j] == -1:
						a[pos_i][pos_j] = 0
						[pos_i, pos_j, value] = stack.pop()
						a[pos_i][pos_j] = find_valid(pos_i,pos_j,value)
					stack.append([pos_i,pos_j,a[pos_i][pos_j]])
					i,j = pos_i,pos_j
				else:
					a[i][j] = x
					stack.append([i,j,x])
			j += 1
		i += 1
	
sudoku()

for i in range(0,limit):
	for j in range(0,limit):
		print a[i][j],
	print
