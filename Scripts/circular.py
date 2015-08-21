a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
max_u = 0
max_d = 4
max_l = 0
max_r = 4

for each in a:
	for every in each:
		print every,
	print

def goRight(i,j):
	if max_r < max_l or max_u > max_d:
		return
	global max_r, max_l, max_u, max_d
	print a[i][j]
	if j<max_r:
		goRight(i,j+1)
	else:
		max_u += 1
		goDown(i+1,j)

def goLeft(i,j):
	if max_r < max_l or max_u > max_d:
		return
	global max_r, max_l, max_u, max_d
	print a[i][j]
	if j>max_l:
		goLeft(i,j-1)
	else:
		max_d -= 1
		goUp(i-1,j)

def goUp(i,j):
	if max_r < max_l or max_u > max_d:
		return
	global max_r, max_l, max_u, max_d
	print a[i][j]
	if i>max_u:
		goUp(i-1,j)
	else:
		max_l += 1
		goRight(i,j+1)

def goDown(i,j):
	if max_r < max_l or max_u > max_d:
		return
	global max_r, max_l, max_u, max_d
	print a[i][j]
	if i<max_d:
		goDown(i+1,j)
	else:
		max_r -= 1
		goLeft(i,j-1)

goRight(0,0)
