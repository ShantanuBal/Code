# n-queens

a = 	[
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0]
	]

n = len(a)
stack = [[0,-1]]

def clear(i,j):
	global a
	for p in range(n):
		if a[p][j] == 1:
			return 0
		if a[i][p] == 1:
			return 0
	
	x, y = i+1, j+1
	while x<n and y<n:
		if a[x][y] == 1:
			return 0
		x += 1; y += 1
	
	x, y = i-1, j-1
	while x>-1 and y>-1:
		if a[x][y] == 1:
			return 0
		x -= 1; y-= 1

	x, y = i-1, j+1
	while x>-1 and y<n:
		if a[x][y] == 1:
			return 0
		x -= 1; y += 1

	x, y = i+1, j-1
	while x<n and y>0:
		if a[x][y] == 1:
			return 0
		x += 1; y -= 1
	
	return 1

def is_possible(lev, pos):
	global a
	for j in range(pos+1, n):
		if clear(lev,j):
			a[lev][j] = 1
			return j
	else:
		return -1


def n_queens():
	global a, stack
	while len(stack) <= n:
		#print stack
		[lev, pos] = stack.pop()
		if pos != -1:
			a[lev][pos] = 0
		nex = is_possible(lev, pos)
		if nex != -1:
			stack.append([lev, nex])
			stack.append([lev+1, -1])

n_queens()

for each in a:
	print each
