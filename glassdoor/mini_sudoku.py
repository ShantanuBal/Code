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
				a[i][j] = find_valid(i,j,a[i][j])
				while a[i][j] == -1:
					a[i][j] = 0
					[i, j, value] = stack.pop()
					a[i][j] = find_valid(i,j,a[i][j])
				stack.append([i,j,a[i][j]])
			j += 1
		i += 1
	
sudoku()

for i in range(0,limit):
	for j in range(0,limit):
		print a[i][j],
	print
