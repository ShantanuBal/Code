# number of ways of going from left top corner to right bottom corner

r,c = 10,5
count = 0

def find_path(i,j):
	global count
	if i==r and j==c:
		count += 1; return
	if i < r:
		find_path(i+1, j)
	if j < c:
		find_path(i, j+1)

find_path(0,0)
print count
